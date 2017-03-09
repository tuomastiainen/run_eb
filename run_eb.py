#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
import ast


class EBApp():

    def __init__(self):
        self.capture_envs()

    def capture_envs(self):
        en = subprocess.check_output(["eb", "list", "--verbose"])
        self.envs = {i.split(":")[0].strip(): ast.literal_eval(
            i.split(":")[1].strip()) for i in en.split('\n') if " : " in i}
        # print(self.envs)

    def run_command(self, env, command):
        e = self.envs[env]
        for i in e:
            print("Instance " + i)
            command_s = " ".join(command)
            print("eb ssh " + env + " -i " + i + " --command " + command_s)
            en = subprocess.check_output(
                ["eb", "ssh", env, "-i", i, "--command", command_s])


if __name__ == "__main__":
    try:
        env = (sys.argv[1])
        command = (sys.argv[2:])
    except IndexError:
        print("Usage: python run_eb.py <environment_name> <command>")
        quit()

    e = EBApp()
    e.run_command(env, command)
