<div align="center">

# ◐ &nbsp; Diagram Magix &nbsp; ◑

**Easily Generate any kind of Diagram with just a simple description.**

<p>
<a href="https://github.com/agaraman0/Diagram-Magix/commits"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/agaraman0/Diagram-Magix" /></a>
<a href="https://github.com/agaraman0/Diagram-Magix/issues"><img alt="GitHub Issues" src="https://img.shields.io/github/issues/agaraman0/Diagram-Magix" /></a>
<a href="https://github.com/agaraman0/Diagram-Magix/pulls"><img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/agaraman0/Diagram-Magix" /></a>
<a href="https://github.com/agaraman0/Diagram-Magix/blob/main/LICENSE"><img alt="Github License" src="https://img.shields.io/badge/License-MIT-green.svg" /></a>
<a href="https://github.com/agaraman0/Diagram-Magix"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/agaraman0/Diagram-Magix?style=social" /></a>
</p>

<br />

</div>

If you've ever faced the need of creating diagrams for a specific use case, this project is for you. 

with the collective brilliance of the OSS community and the current state of LLMs, it's now possible to generate a diagram just from a description.

## ⚡️ Usage

1. Install Docker and ensure that it's running. It's also recommended that you use at least GPT-4, or GPT-3.5-turbo.

## 📦 Setup

1. Install docker and docker-compose

2. Once docker is installed, navigate to the project directory and update your OPENAI_API_KEY inside `docker-compose.dev.yml`

This will export your OPENAI_API_KEY inside the docker environment and install all the necessary dependencies in that environment.

3. Run the command in the following order

```bash
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up
```

4. if you want to stop the docker container setup 

```bash
docker-compose -f docker-compose.dev.yml down
```


## 🤖 How it Works


### 📝 Prompt Design


## 📈 Performance

Diagram Magix is currently hosted and accessible at www.devf.in . As we are using GPT APIs for recipe generation so currently latency is high somewhere Avg of 50 seconds to 60 seconds. we are currently adding and building it to make it more robust.

## ✅ Benchmarks



## 🧗 Roadmap


## 📣 Call to Action

if you are looking to contribute or have found some issues raise a pull request or create an issue

