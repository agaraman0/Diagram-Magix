import React, { useRef, useState } from 'react';
import { renderToString } from 'react-dom/server';
import { ReactSVG } from 'react-svg';
import { Button, TextField, Box, CircularProgress, AppBar, Toolbar, Typography, Container, Grid, Paper, Link, IconButton } from '@mui/material';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import TwitterIcon from '@mui/icons-material/Twitter';
import GitHubIcon from '@mui/icons-material/GitHub';
import axios from 'axios';

// Header Component
const Header = () => (
  <AppBar position="static" color="primary">
    <Toolbar>
      <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
        Diagram Designer
      </Typography>
      <IconButton color="inherit" href="https://www.linkedin.com/in/agaraman0">
        <LinkedInIcon />
      </IconButton>
      <IconButton color="inherit" href="https://twitter.com/aman_agarwal0">
        <TwitterIcon />
      </IconButton>
      <IconButton color="inherit" href="https://github.com/agaraman0/Diagram-Magix">
        <GitHubIcon />
      </IconButton>
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
  const svgRef = useRef(null);

  const handleDesignClick = async () => {
    setIsLoading(true);

    try {
      const response = await axios.post('/call_prompt',
        {
          input: description,
        },
        {
          headers: { "Content-Type": "application/json" },
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
  const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
  const svgUrl = URL.createObjectURL(svgBlob);

  const downloadPNG = () => {
    const svgString = renderToString(svgRef.current);
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();

    img.src = `data:image/svg+xml;base64,${btoa(svgString)}`;
    img.onload = () => {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);
      const pngUrl = canvas.toDataURL();
      const link = document.createElement('a');
      link.href = pngUrl;
      link.download = 'diagram.png';
      link.click();
    };
  };

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
              {isLoading ? <CircularProgress /> : <ReactSVG src={svgUrl} ref={svgRef} />}
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
                <>
                  <Link href={svgUrl} download="diagram.svg" sx={{ mt: 2, display: 'block' }}>
                    Download Diagram (SVG)
                  </Link>
                  <Button onClick={downloadPNG} sx={{ mt: 2, display: 'block' }}>
                    Download Diagram (PNG)
                  </Button>
                </>
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
