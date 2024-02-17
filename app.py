import aws_cdk as cdk

app = cdk.App()
stack = cdk.Stack(app, "cdk-ec2-windows-stack")

# VPC
VPC_CIDR = "10.141.0.0/16"  # お好みで変更ください
vpc = cdk.aws_ec2.Vpc(
    stack,
    "vpc",
    cidr=VPC_CIDR,
    max_azs=1,
    subnet_configuration=[
        cdk.aws_ec2.SubnetConfiguration(
            name="public",
            subnet_type=cdk.aws_ec2.SubnetType.PUBLIC,
        ),
    ],
)

# EC2
key_pair = cdk.aws_ec2.KeyPair(stack, "keyPair")
instance = cdk.aws_ec2.Instance(
    stack,
    "instance",
    vpc=vpc,
    vpc_subnets=cdk.aws_ec2.SubnetSelection(subnet_type=cdk.aws_ec2.SubnetType.PUBLIC),
    # instance_type=cdk.aws_ec2.InstanceType.of(cdk.aws_ec2.InstanceClass.T2, cdk.aws_ec2.InstanceSize.MICRO),
    instance_type=cdk.aws_ec2.InstanceType.of(cdk.aws_ec2.InstanceClass.T3A, cdk.aws_ec2.InstanceSize.MEDIUM),
    machine_image=cdk.aws_ec2.WindowsImage(cdk.aws_ec2.WindowsVersion.WINDOWS_SERVER_2022_JAPANESE_FULL_BASE),
    key_pair=key_pair,
    ssm_session_permissions=True,
)

app.synth()
