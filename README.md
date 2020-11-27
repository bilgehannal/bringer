# bringer

Bringer is a command line tool that tries to make faster your development process. You can write the keywords and you can get the script, command or information that you need using your terminal screen.

* Practical Usage
* Easy contribution for dataset
* Faster development process.

### How to use?

To install: `pip install bringer`

https://pypi.org/project/bringer/

You can add labels that you want to give after the command of bringer like:

    bringer base64 encryption
    bringer k8s ssvc yaml template

Example:

```
$ bringer k8s external svc yaml template
apiVersion: v1
kind: Service
metadata:
  name: $project_name
spec:
  externalName: $project_name.$namespace.svc.cluster.local
  ports:
    - port: $port
  type: ExternalName
```
### How it works?
There is a simple python script running in background of the 'bringer'. It takes all the parameters as a label and it compares those labels to other labels in the dataset. It gets the content of the best match from dataset.

### Contribution for dataset

Github Repository of Dataset: https://github.com/bilgehannal/bringer-data

* Add your data into the [content directory](https://github.com/bilgehannal/bringer-data/tree/main/contents)
* Add a description for your data into the file named [content.yaml](https://github.com/bilgehannal/bringer-data/blob/main/content.yaml)
* Open a pull request.
* That's all.