#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml


def main():
    with open('my-job.yml', 'r') as stream:
        try:
            job = yaml.load(stream)
            # print(type(job))
            print(job['email'])
            print(job['step2'])
        except yaml.YAMLError as e:
            print(e)


def send_email():
    # TODO
    print("Sending email")

if __name__ == '__main__':
    main()
