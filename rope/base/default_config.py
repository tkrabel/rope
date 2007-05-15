# The default ``config.py``


def set_prefs(prefs):
    """This function is called before the project is opened"""

    # Specify which files and folders to ignore in the project.
    # Changes to ignored resources are not added to the history and
    # VCSs.  Also they are not shown in "Find File" dialog.
    prefs['ignored_resources'] = ['*.pyc', '.svn', '*~', '.ropeproject']

    # This option tells rope how to hold and save object information.
    # Possible values are:
    #
    # * 'memory': It holds all information in
    #   memory.  So it is the fastest and the least memory efficient.
    #   Its biggest problem is that the data is not saved and
    #   the information is lost when you open a project in future.
    #   You probably never want to use this (it is used in unit
    #   tests), but if you decide not to have rope folder (see ~/.rope
    #   file) this db is used.
    #
    # * 'persisted_memory': Exactly like 'memory' but the information is
    #   saved for future sessions.  The problem with this approach is
    #   that it might take lots of memory (This is not an issue for
    #   small projects).  It might also make opening and closing
    #   projects a bit slower.
    #
    # * 'shelve': It stores data in `shelve` files.  This solves
    #   both the memory efficiency and the persistency problems.  But
    #   `shelve` is known to cause misterious problems in rare
    #   conditions.
    #
    # * 'sqlite': It uses `sqlite3` module which is available in
    #   Python distributions starting from ``2.5``.  It is like
    #   'shelve' but probably more reliable.  But it is much less CPU
    #   efficient.
    #
    # The choice of the objectdb might be hard.  For small
    # projects I think 'persisted_memory' is the best.  For larger
    # projects I prefer 'shelve'.  If you encounter mysterious
    # problems when using 'shelve' use the slower 'sqlite'.
    prefs['objectdb_type'] = 'persisted_memory'

    # Shows whether to save history across sessions.  Defaults to
    # `False`.
    prefs['save_history'] = True
    prefs['max_history_items'] = 100

    # If `False` when running modules or unit tests "Dynamic Object
    # Inference" is turned off.  This makes them much faster.  The
    # default is `True`.
    prefs['perform_doi'] = True

    # Rope can test the validity of its object DB when running.  You
    # can turn this feature off by using `False`.  Defaults to
    # `True`.
    prefs['validate_objectdb'] = True

    # If `True`, rope will analyze each module when it is saved.
    prefs['automatic_soi'] = True

    # Set the number spaces used for indenting.  According to
    # :PEP:`8`, it is best to use 4 spaces.  Since most of rope's
    # unit-tests use 4 spaces it is more reliable, too.
    prefs['indent_size'] = 4


def project_opened(project):
    """This function is called after the project is opened"""
    # Do whatever you like here!