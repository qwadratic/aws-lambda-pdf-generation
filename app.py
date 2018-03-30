import subprocess
import boto3
from chalice import Chalice
from jinja2 import Template

app = Chalice(app_name='html2pdf')
s3 = boto3.client('s3', region_name='eu-central-1')
BUCKET = 'bulyatestlambda'


@app.route('/url2pdf', methods=['POST'])
def url2pdf():
    try:
        request = app.current_request
        ctx = request.json_body['template_context']
        tpl = Template('<html>Hello {{ name }}!</html>')
        html = tpl.render(ctx)
        proc = subprocess.run(
            ["./wkhtmltopdf2", "-", "-"],
            input=bytes(html, encoding="utf-8"),
            stdout=subprocess.PIPE,
        )
        pdf = str(proc.stdout)
        key = 'test.pdf'

        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=pdf,
            ACL='public-read',
        )
        return {
            "pdf_url": "https://{}.s3.amazonaws.com/{}".format(BUCKET, key)
        }
    except Exception as e:
        return {'error': str(e)}
