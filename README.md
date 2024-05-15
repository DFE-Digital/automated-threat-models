# Automated Threat Models

Threat modelling can become time consuming, and doing a thorough threat model for every single service is not scalable when taking into account security resources and the number of services in operation at DfE.

This repo attempts to produce a working example of how one could partly automate the threat modelling process for some of our lower risk services.

As part of secure by design principles we should be:

* running threat models for every service
* producing the results and reporting them

This example is based on a real service called [service-security-posture-hardening (run as an internal tool by CISD)](https://github.com/DFE-Digital/service-security-posture-hardening). 

The [main tool used is called threagile](https://github.com/Threagile/threagile), and it is run as a docker container. 

Using GitHub Actions, Docker, and Splunk, we can continuously watch the yaml file that holds the data for your threat model, and when changes are made, they produce new reports that can be ingested into Splunk.

This method:

* removes the need for a security resource and long sessions
* ensures the data can be kept up to date when mitigations are implemented, allowing it to be tracked effectively
* gives a basic understanding of potential threats a system might face by producing output based on information given in a yaml file
* produces data flow diagrams that may be useful not just in threat modelling, but also architectural decisions and audit requirements

## Getting started with an initial threat model YAML

### Pre-requisites (local)

Before getting started, you will need to:

* install docker
* [pull the container image from GitHub Packages](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) by:
    * creating a personal access token with `read:packages` permission scoped to the DfE-Digital org
    * setting your PAT token as an enviornment variable: `export CR_PAT=YOUR_TOKEN`
    * logging in with docker: `echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin`
    * pulling the image: `docker pull ghcr.io dfe-digital/automated-threat-models`
* data from Splunk regarding your Azure resources including: name, kind, type (s1XXX-functionX, functionapp, microsoft.web/sites) **note that this is to be automated in the next iteration**

### Automated threat models (DfE)

This project's main purpose is to enable DfE to run continuous automated threat models, which data can be ingested by the continuous assurance platform.

The automated threat models will be kept in the [continuous assurance private repo](https://github.com/DFE-Digital/service-security-posture-hardening-private), which will query this project.

The automation is based on dfe-threagile being able to read data regarding Azure resources in Splunk.

Basic usage: 

##### Run DfE automation
```shell
$ docker run --rm -it -v "$(pwd)":/app/work --entrypoint python dfe-digital/automated-threat-models dfe_threagile.py
```

### Create a stub model and example model (manual)

It's advisable to create a stub and example model from threagile to give you a framework YAML file to work with and a thorough example with hints you can copy.

#### Create a stub
```shell
$ docker run --rm -it -v "$(pwd)":/app/work threagile/threagile -create-stub-model -output /app/work
```

#### Create an example

```shell
$ docker run --rm -it -v "$(pwd)":/app/work threagile/threagile -create-example-model -output /app/work
```

#### Use a schema or template in your IDE
```shell
$ docker run --rm -it -v "$(pwd)":/app/work threagile/threagile -create-editing-support -output /app/work
```

### Using hints, comments and macros

When writing your YAML file, there will be fields you need to fill that must have a value from a limited list, or they should link to another object you've created (linked by the id field). 

In order to assist you, there are a few things that can help you, such as:

* comments on many of the lines in the [example model](threagile-example-model.yaml)
* type values list for each field that you can check by running `$ docker run --rm -it threagile/threagile -list-types`
* macros that you can run, that will take you through a wizard to produce a objects in your YAML based on your answers

The macros available are for:

```
----------------------
Built-in model macros:
----------------------
add-build-pipeline --> Add Build Pipeline
add-vault --> Add Vault
pretty-print --> Pretty Print
remove-unused-tags --> Remove Unused Tags
seed-risk-tracking --> Seed Risk Tracking
seed-tags --> Seed Tags
```

The "Add Build Pipeline" is especially useful, as it will allow you to add all your assets relating to GitHub, Azure Devops, Kubernetes, Docker Hub, packages etc.

To run a macro you will need to run: 

```shell
$ docker run --rm -it -v "$(pwd)":/app/work threagile/threagile -model /app/work/threagile.yaml -output /app/work -execute-model-macro <NAME>
```


### Filling in the YAML with your system data

Start by filling in the metadata at the top with information about the service and yourself. Ensure you add useful tags, and that you keep tags consistent throughout the doc, so if you put `azure-function-app` in your main list of tags, when creating a technical asset that's a function app, use the same tag.

Then work your way down the YAML. The YAML consists of:

* initial metadata
* data assets (e.g. actual data you hold: keys, school records, usernames)
* technical assets (e.g. function app, github repo, CI/CD, K8s)
    * technical assets are large objects, so ensure you refer to the comments in your example model
    * there are communication links attached that are used to build the data flows
* trust boundaries (e.g. network boundaries, different cloud hosts - github, azure, DfE network)
* shared runtimes (e.g. k8s)
* individual risk categories (this could be a risk that you think can't be linked to assets you've listed, but something you know you're concerned about)
* risk tracking (this is where you track your risks and mitigations)

**Make sure to refer to your example, as well as the model produced in this repository (which is a real world DfE app). This will be crucial in understanding how to build your own**

## Producing your initial threat model output

Once you've produced your YAMl model, you will need to run the command shown below to produce your outputs:

```shell
$ docker run --rm -it -v "$(pwd)":/app/work threagile/threagile -verbose -model /app/work/YOUR_YAML.yaml -output /app/work
```

If you're happy with the outputs, and would like to start tracking your risks/mitigations, you can run the python script in this repo to produce the YAML required for the bottom section of your YAML file:

```shell
$ python3 produce_risk_tracker.py
``` 
(default values currently hardcoded)

The output it provides comes from your risks.json that threagile produces, and puts it in the format required for the risk tracking section at the bottom of your YAML, simply copy and paste the output. You can then rerun it and the risks will be updated in the reporting outputs.

**IMPORTANT: Changes are only shown in the empty columns on the risks sheet once you change the status from "unchecked" as they relate to you reviewing the issue**

# TODO / Roadmap

- [x] example GitHub Action to watch file
- [x] use params for python
- [ ] improve readme
- [x] automate more of the yaml building beyond what threagile can do
- [ ] automate the Azure data ingestion from Splunk
