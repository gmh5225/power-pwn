import logging

from art import tprint

from powerpwn.cli.arguments import parse_arguments
from powerpwn.cli.const import LOGGER_NAME
from powerpwn.cli.runners import (
    run_backdoor_flow_command,
    run_dump_command,
    run_gui_command,
    run_nocodemalware_command,
    run_phishing_command,
    run_recon_command,
)

logger = logging.getLogger(LOGGER_NAME)


def main():
    print("\n\n------------------------------------------------------------")
    tprint("powerpwn")
    print("------------------------------------------------------------\n\n")

    args = parse_arguments()

    logging.basicConfig(level=args.log_level, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger.level = args.log_level
    command = args.command

    if command == "dump":
        run_dump_command(args)
    elif command == "recon":
        run_recon_command(args)
    elif command == "gui":
        run_gui_command(args)
    elif command == "backdoor":
        run_backdoor_flow_command(args)
    elif command == "nocodemalware":
        run_nocodemalware_command(args)
    elif command == "phishing":
        run_phishing_command(args)
    else:
        logger.info("Run `powerpwn --help` for available commands.")


if __name__ == "__main__":
    main()
