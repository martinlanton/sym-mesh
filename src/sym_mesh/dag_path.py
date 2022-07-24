from maya.api import OpenMaya as om2


def create_MDagPath(path_to_dag_object):
    """

    :param path_to_dag_object: path to the dag object for which we want the MDagPath.
    :type path_to_dag_object: str

    :return: MDagPath of the object at the specified path or None.
    :rtype: MDagPath
    """
    selection_list = om2.MSelectionList()
    try:
        selection_list.add(path_to_dag_object)
    except:
        return None
    dag_path = selection_list.getDagPath(0)

    return dag_path
