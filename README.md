# Docker Dask Workbench

## Vision

This project is simple Docker configuration to test Dask


## Ethics

This project operates under the W3C's
[Code of Ethics and Professional Conduct](https://www.w3.org/Consortium/cepc):

> W3C is a growing and global community where participants choose to work
> together, and in that process experience differences in language, location,
> nationality, and experience. In such a diverse environment, misunderstandings
> and disagreements happen, which in most cases can be resolved informally. In
> rare cases, however, behavior can intimidate, harass, or otherwise disrupt one
> or more people in the community, which W3C will not tolerate.
>
> A Code of Ethics and Professional Conduct is useful to define accepted and
> acceptable behaviors and to promote high standards of professional
> practice. It also provides a benchmark for self evaluation and acts as a
> vehicle for better identity of the organization.

We hope that our community group act according to these guidelines, and that
participants hold each other to these high standards. If you have any questions
or are worried that the code isn't being followed, please contact the owner of the repository.


## Language

The development language is English. 
All comments and documentation should be written in English, 
so that we don't end up with “franglais” methods, and so 
we can share our knowledge with developers around the world.

However, the domain language is French. 
We consider each tax, collecting organism and French regulation as a domain-specific term. 
In the same fashion, well-known abbreviations of these domain-specific terms are accepted.

**OR**

Par souci de lisibilité pour les partenaires, la langue utilisée 
pour la description et le suivi de fonctionnalités est le français.

En revanche, pour éviter le coût du changement de contexte, 
les discussions techniques peuvent se faire en anglais, 
la langue la plus utilisée dans le cadre du développement logiciel.

## Installation

We're using these technologies: 

- Github
- Docker
- Docker-Compose

Once installed, you have to run these commands to setup the project:

```shell
docker-compose up
```

To access to the web interface, open your browser and enter this address:
- `http://127.0.0.1:8787` to see Dask distributed WebUI.
- `http://127.0.0.1:8888` to see Jupyter Lab WebUI.

Enjoy!

## Contributing



### Development

We're really happy to accept contributions from the community, 
you will have more information in [CONTRIBUTE](CONTRIBUTE.md) file! 
There are many ways to contribute, 
even if you're not a technical person.

We're using the [Github flow](https://guides.github.com/introduction/flow/) 
to accept modifications (even internally), 
basically you'll have to:

1. Create an issue related to the problem you want to fix (good for traceability and cross-reference).
2. Create a branch (optionally with the reference to the issue in the name).
3. Hack hack hack.
4. Commit incrementally with readable and detailed commit messages.
5. Submit a pull-request against the develop branch of this repository.

### What happens next? How to deploy?

Deployment is almost automated, you just have to validate a release on Github to deploy.

1. When your pull-request is created, it runs the CI workflow, this workflow is run everytime a commit is added to the pull-request.
2. Review, comment, reject or accept the pull-request.
3. When your pull-request is merged, it runs the Build workflow against the base branch to generate the `base_ref` images.
4. If the workflow succeed, a new tag will be tag to the commit merged.
5. Edit the tag, copy the tag version as release name (and check pre-release if you want to deploy to staging). 

If you're not familiar with open-source workflows or our set of technologies, 
do not hesitate to ask for help! We can mentor you or propose good first bugs 
(as labeled in our issues). 
Also welcome to add your name to Credits section of this document.

### Submitting bugs

You can report issues directly on Github, 
that would be a really useful contribution given that we lack some 
user testing on the project. 
Please document as much as possible the steps 
to reproduce your problem (even better with screenshots).

### Discussing strategies

We're trying to develop this project in the open as much as possible. 
We have a dedicated mailing-list where we discuss each new strategic 
change and invite the community to give a valuable feedback. 
You're encouraged to subscribe to it and participate.

### Adding documentation

We're doing our best to document each usage of the project 
but you can improve it or add you own sections. 
The documentation is available within the /docs/ folder. 
You don't have to build anything, we'll take care of it once your changes are merged.

### Hacking backend

Hello fellow hacker, it's good to have you on board! 

You have to run tests periodically though to ensure that your changes don't break existing features. 
Our continuous integration server will run the whole test suite once you submit your pull-request (approx. 5 minutes).

- Commit messages should be formatted using [AngularJS conventions](http://goo.gl/QpbS7) (one-liners are OK for now but body and footer may be required as the project matures).
- PRs should follow these [8 Tips for Great Code Reviews](https://kellysutton.com/2018/10/08/8-tips-for-great-code-reviews.html).

## Versioning

Version numbering follows the [Semantic versioning](http://semver.org/) approach.

## License

You will have more information in [LICENSE](LICENSE) file
