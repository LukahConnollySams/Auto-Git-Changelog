<h1>auto-git-changelog</h1>

<h2>About</h2>
<p>This project aims to provide a simple solution to three things using python scripts and git hooks: <p>
<ol>
    <li>Auto version tagging/bumping</li>
    <li>Auto changelog generation</li>
    <li>Keeping the non python programming to a minimum whilst completing 1 and 2</li>
</ol>

<p>Currently this does not have full Functionality, and is in a developement phase. At the moment the functionality includes running only bumping the version of the project using the commit message.</p>


<h2>How it works</h2>


<h3>Version and Changlelog:</h3>
<p>For auto version tagging and changelog generation, python scripts used to handle the string parsing, and are then called by bash scripts inside the ".git/hooks" folder during the post-commit.</p>
<p>A changlelog file must already exist prior to use, and the scripts will not backtrack through the git log (will only parse the most recent commit). Scripts require poetry, and a pyproject.toml, or similar file for use.</p>
