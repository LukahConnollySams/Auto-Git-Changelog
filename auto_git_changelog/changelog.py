from . import changelog_file, changelog_template, changelog_version_template
from jinja2 import Template
from datetime import datetime
import bs4


def version_check(version: str, changelog_file: str=changelog_file) -> bool:

    version_id = bs4.SoupStrainer(id=version)
    has_id = bool(bs4.BeautifulSoup(changelog_file, 'html.parser', parse_only=version_id))

    if has_id:

        return True


    else:

        return False

    
def write(version: str, msg: str, changelog_file: str=changelog_file) -> None:

    changelog_soup = bs4.BeautifulSoup(changelog_file, 'html.parser')

    if not version_check(version, changelog_file):

        write_version_header(version)

    write_commit_msg(msg)
    

def write_commit_msg(msg: str):
    
    # write rendered template to file
    changelog_msg = changelog_template.render(date=datetime.today().strftime('%Y-%m-%d %H:%M::%S'), message=msg)

    


def write_version_header(version):

    # write rendered version template to file
    changelog_version_header = changelog_version_template.render(version=version)

    