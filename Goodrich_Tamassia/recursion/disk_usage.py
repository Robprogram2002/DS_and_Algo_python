import os


# Given the recursive nature of the file-system representation, it should not come as a surprise that many common
# behaviors of an operating system, such as copying a directory or deleting a directory, are implemented with recursive
# algorithms. In this section, we consider one such algorithm: computing the total disk usage for all files and
# directories nested within a particular directory.

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""
    total = os.path.getsize(path)  # account for direct usage
    if os.path.isdir(path):  # if this is a directory,
        for filename in os.listdir(path):  # then for each child:
            child_path = os.path.join(path, filename)  # compose full path to child
            total += disk_usage(child_path)  # add child’s usage to total

    print('{0: < 7}'.format(total), path)  # descriptive output (optional)
    return total
