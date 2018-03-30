# aws-lambda-pdf-generation
Generate PDF files with custom content from HTML templates

### Requirements
- AWS account credentials

### Install deps

```bash
pip install git+https://github.com/qoda/python-wkhtmltopdf.git
pip install -r requirements.txt
```

### Deploy to Lambda

```bash
mkdir ~/.aws
cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)

chalice deploy
```
