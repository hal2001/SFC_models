"""
build_run_all_scripts.py

Build the file 'run_all_scripts.py'. Used to validate that all scripts run without crashing.

Currently, no attempt to validate output; that's the job of unit tests.


Copyright 2017 Brian Romanchuk

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

def main():
    f_in = open('script_list.txt', 'r')
    f_out = open('run_all_scripts.py', 'w')
    f_out.write('"""\n')
    f_out.write('Machine-generated file used to validate that all scripts run without crashing.\n')
    f_out.write('Generated by build_run_all_scripts.py\n')
    f_out.write('Have a nice day!\n')
    f_out.write('"""\n\n\n')
    f_out.write('from __future__ import print_function\n')
    f_out.write('import sfc_models.examples.Quick2DPlot as extras\n')
    f_out.write('extras.plt = None # Prang the plots\n\n\n')
    for fname in f_in:
        fname = fname.strip()
        if not fname.endswith('.py'):
            raise ValueError('Bad file in script_list.txt')
        fname = fname[:-3]
        f_out.write('import {0}\n'.format(fname))
        f_out.write('if "main" in dir({0}):\n'.format(fname))
        f_out.write('    {0}.main()\n'.format(fname))
        f_out.write('\n\n')


if __name__=='__main__':
    main()