import sys
import changelog
import version


def main():

    commit_msg: str = sys.argv[0]

    new_version = version.bump_version(commit_msg)

    print(new_version)


if __name__ == "__main__":

    main()