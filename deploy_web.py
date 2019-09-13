import argparse
import sys
import subprocess

def yes_or_no(question):
    '''
    Asks a question on prompt, waits for y/n
    Input: question, string
    Output: True/False
    '''
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

def run_shell_cmd(cmd):
    '''
    Runs a command on shell
    Input: cmd, string
    Output: Tuple (True/False, empty-list/stderr-string-list)
    '''
    proc = subprocess.Popen(cmd, shell=True,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    return_code = proc.wait()
    if not return_code:
        for line in proc.stdout.readlines():
            print(line)
        return (True, [])
    else:
        return (False, proc.stderr.readlines())

def main(prod):
    '''
    Main entrypoint
    Input:prod, boolean to indicate production deploy
    '''
    if prod:
        if yes_or_no("Deploying to prod, are you sure?"):
            print("Deploy to prod now...")
        else:
            print("Bye..")
            sys.exit(0)
    else:
        print("Deploy to staging now...")
        cmd = "gsutil rsync -x '\.DS_Store' -R web/ gs://staging.hodlboard.com"
        done, outlist = run_shell_cmd(cmd)
        if done:
            print("Completed")
            sys.exit(0)
        else:
            for line in outlist:
                print("FAILED!")
                print(line)
                sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Deploy Static Site')
    parser.add_argument('--production', required=False,
                        action='store_true',
                        help='deploy to production')
    args = parser.parse_args()
    main(prod=args.production)
