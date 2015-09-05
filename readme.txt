git-ascii-bundle-create <gitRepo> <bundlePath> [<exclusionCommit>]

Takes the specified <gitRepo> and writes out files at <bundlePath> which can be used
to re-form the original commits, files, and trees. These files are human-readable (unless
you have binary data in your repository).

If <exclusionCommit> is specified, then any file/tree/commit present at the time of the
specified commit will not be included in the bundle.



git-ascii-bundle-imbue <bundlePath> <gitRepo> <branchName>

Creates a branch named <branchName> in the repository at <gitRepo> and imports all objects
contained in the bundle at <bundlePath>.

Note that the repository should be free from any modifications, staged data, or untracked
files before performing this operation. Furthermore, in some circumstances, the git
repository may need to have 'git reset --hard' called on it after this operation.



git-tree-decode <treeFile> <outputFile>

Decodes the output of 'git cat-file tree <id>' (as stored in <treeFile>) to be human
readable (stored in <outputFile>) but convertible back to the original binary form.



git-tree-encode <treeFile> <outputFile>

Encodes the human-readable file (created above, as stored in <treeFile>) into the binary
format used by git (stored in <outputFile>) which can then be passed into
'git hash-object -w -t tree <outputFile>'



git-ascii-bundle-verify <bundlePath>

Runs every object file in <bundlePath> through 'git hash-object' appropriately and checks
the results.