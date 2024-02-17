import aws_cdk as cdk

app = cdk.App()
stack = cdk.Stack(app, "cdk-ec2-windows-stack")

# ここに必要なリソース書く

app.synth()
