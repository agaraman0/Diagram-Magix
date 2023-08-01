import React, { useState } from 'react';
import { Button, TextField, Box, CircularProgress, AppBar, Toolbar, Typography, Container, Grid, Paper, Link } from '@mui/material';
import axios from 'axios';

// Header Component
const Header = () => (
  <AppBar position="static" color="secondary">
    <Toolbar>
      <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
        Diagram Designer
      </Typography>
    </Toolbar>
  </AppBar>
);

// Footer Component
const Footer = () => (
  <Box sx={{ p: 2, mt: 'auto', backgroundColor: 'background.paper' }}>
    <Typography variant="body2" color="text.secondary" align="center">
      {'© '}
      {new Date().getFullYear()}
      {' Diagram Designer.'}
    </Typography>
  </Box>
);

// Main App Component
function App() {
  const [description, setDescription] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [svgData, setSvgData] = useState(null);

  const handleDesignClick = async () => {
    setIsLoading(true);

    try {
      const response = await axios.post('/call_prompt', 
        {
          input: description,
        },
        {
          headers: {"Content-Type": "application/json"},
          redirect: 'follow'
        }
      );

      setSvgData(response.data);
    } catch (error) {
      console.log("here is svg", error.code, error.response)
      setSvgData(error.response.data)
    }

    setIsLoading(false);
  };

  // Creating a Blob from SVG data
  const svgBlob = new Blob([svgData], {type: 'image/svg+xml;charset=utf-8'});
  const svgUrl = URL.createObjectURL(svgBlob);

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
      }}
    >
      <Header />

      <Container component="main" sx={{ mt: 8, mb: 2 }} maxWidth="lg">
        <Grid container spacing={2}>

          <Grid item xs={12} sx={{ minHeight: '50vh', bgcolor: 'background.paper' }}>
            <Box
              sx={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                width: '100%',
                height: '100%',
                border: '1px solid',
                borderColor: 'divider',
                overflow: "auto",
              }}
            >
              {isLoading ? <CircularProgress /> : <div dangerouslySetInnerHTML={{ __html: svgData }} />}
            </Box>
          </Grid>

          <Grid item xs={12}>
            <Paper variant="outlined" sx={{ p: 2, bgcolor: 'background.paper' }}>
              <TextField
                label="Diagram description"
                variant="outlined"
                fullWidth
                value={description}
                onChange={(event) => setDescription(event.target.value)}
              />

              <Button
                variant="contained"
                color="primary"
                fullWidth
                onClick={handleDesignClick}
                disabled={isLoading}
                sx={{ mt: 2 }}
              >
                Design Diagram
              </Button>

              {!isLoading && svgData && (
                <Link href={svgUrl} download="diagram.svg" sx={{ mt: 2, display: 'block' }}>
                  Download Diagram
                </Link>
              )}
            </Paper>
          </Grid>
        </Grid>
      </Container>

      <Footer />
    </Box>
  );
}

export default App;
