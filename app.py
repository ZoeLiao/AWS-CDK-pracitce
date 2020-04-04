#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_pracitce.aws_cdk_pracitce_stack import AwsCdkPracitceStack


app = core.App()
AwsCdkPracitceStack(app, "aws-cdk-pracitce")

app.synth()
