import board, argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command',help='commands')
    boards=board.Board()
    
    update=sub_parsers.add_parser("update",help="update <row> <column> (0-2)")
    update.add_argument("row",type=int)
    update.add_argument("col",type=int)
    update.set_defaults(func=boards.update_board)

    display=sub_parsers.add_parser("display",help="displays the board")
    display.set_defaults(func=boards.display_board)

    reset=sub_parsers.add_parser("reset",help="resets the board")
    reset.set_defaults(func=boards.reset_board)

    args=parser.parse_args()
    
    if args.command == "update":
        args.func(args.row,args.col)

    elif args.command == "display":
        args.func()

    elif args.command == "reset":
        args.func()