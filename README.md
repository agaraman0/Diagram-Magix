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

If you've ever faced the need of creating diagrams for specific usecase, this project is for you. 

https://user-images.githubusercontent.com/25165841/250232917-bcc99ce8-99b7-4e3d-a653-f89e163ed825.mp4

with the collective brilliance of the OSS community and the current state of LLMs, it's now possible to generate diagram just from a description.

## ⚡️ Usage

1. Install Docker and ensure that it's running. It's also recommended that you use at least GPT-4, or GPT-3.5-turbo.

## 📦 Setup

1. Install dokcer and docker-compose

2. Once docker is installed, navigate to the project directory and update your OPENAI_API_KEY inside `docker-compose.dev.yml`

This will export your OPENAI_API_KEY inside docker environment and install all the necessary dependencies in that environment.

3. Run the command in following order

```bash
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up
```

4. if you want to stop docker container setup 

```bash
docker-compose -f docker-compose.dev.yml down
```


## 🤖 How it Works


### 📝 Prompt Design


```python
prompt = prompt_constructor(HIERARCHY, GUIDELINES, WRITE_CODE, DEBUG_TESTFILE, SINGLEFILE).format(targetlang=targetlang,buggyfile=buggyfile)
```

## 📈 Performance

Diagram Magix is currently hosted and accesible at www.devf.in . as we are using GPT apis for recipe generation so currently latency is high somewhere Avg of 50 seconds to 60 seconds. we are currently adding and building it make it more robust.

## ✅ Benchmarks



## 🧗 Roadmap


## 📣 Call to Action

if you are looking to contribute or have found some issue raise a pull request or create a issue

