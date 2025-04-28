import os
import subprocess
import argparse

def list_templates():
    print('Available templates:')
    templates = ['MERN', 'LAMP']  # Add more templates if needed
    for template in templates:
        print(f'- {template}')

def run_template(template_name):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates', template_name.lower()))
    if os.path.exists(base_path):
        subprocess.run(['docker-compose', 'up', '--build'], cwd=base_path)
    else:
        print(f'Template {template_name} not found at {base_path}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DevBoxHub CLI')
    parser.add_argument('command', choices=['list', 'run'], help='Command to run')
    parser.add_argument('template', nargs='?', help='Template name')

    args = parser.parse_args()

    if args.command == 'list':
        list_templates()
    elif args.command == 'run' and args.template:
        run_template(args.template)

