<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">clipspeak</h3>

  <p align="center">
    clipspeak is a Python project that synthesizes and speaks text from the clipboard using Azure Cognitive Services.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites


To install clipspeak, you need to have Python 3.6 or higher and pip installed on your system. You also need to have an Azure subscription and a Speech service resource. You can create one [here](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started).
  
### Installation

_Instruction on setup and install._

To install clipspeak from source, clone this repository and run the following command from the root folder:

```bash
pip install .
```

To use clipspeak, you need to create a config file that contains your Azure key and service region. You can also specify different speech configuration sets with different voice names and other options. For example, your config file could look something like this:

```ini
[Azure]
; The default azure key and service region
key = <default_key>
service_region = <default_region>

[Aria]
; The azure key and service region for aria voice
key = <aria_key>
service_region = <aria_region>
; The voice name and pitch for aria voice
voice_name = en-US-AriaNeural
voice_pitch = 0

[Grace]
; The azure key and service region for grace voice
key = <grace_key>
service_region = <grace_region>
; The voice name and pitch for grace voice
voice_name = en-US-GraceNeural
voice_pitch = 0
```

You need to save this config file in a folder named `.config` in your home directory and name it `clipspeak.ini`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run clipspeak, you can use the `clipspeak` command with an optional argument that specifies the speech configuration set to use. For example, to use the aria configuration set, you can run:

```bash
clipspeak -c aria

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the GNU Affero General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
