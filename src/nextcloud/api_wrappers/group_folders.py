# -*- coding: utf-8 -*-
from nextcloud.base import WithRequester


class GroupFolders(WithRequester):
    API_URL = "/apps/groupfolders/folders"
    SUCCESS_CODE = 100

    def get_group_folders(self):
        """
        Return a list of call configured folders and their settings

        Returns:

        """
        return self.requester.get()

    def get_group_folder(self, fid):
        """
        Return a specific configured folder and it's settings

        Args:
            fid (int/str): group folder id

        Returns:

        """
        return self.requester.get(fid)

    def create_group_folder(self, mountpoint):
        """
        Create a new group folder

        Args:
            mountpoint (str): name for the new folder

        Returns:

        """
        return self.requester.post(data={"mountpoint": mountpoint})

    def delete_group_folder(self, fid):
        """
        Delete a group folder

        Args:
            fid (int/str): group folder id

        Returns:

        """
        return self.requester.delete(fid)

    def grant_access_to_group_folder(self, fid, gid):
        """
        Give a group access to a folder

        Args:
            fid (int/str): group folder id
            gid (str): group to share with id

        Returns:

        """
        url = "/".join([str(fid), "groups"])
        return self.requester.post(url, data={"group": gid})

    def revoke_access_to_group_folder(self, fid, gid):
        """
        Remove access from a group to a folder

        Args:
            fid (int/str): group folder id
            gid (str): group id

        Returns:

        """
        url = "/".join([str(fid), "groups", gid])
        return self.requester.delete(url)

    def set_permissions_to_group_folder(self, fid, gid, permissions):
        """
        Set the permissions a group has in a folder

        Args:
            fid (int/str): group folder id
            gid (str): group id
            permissions (int): The new permissions for the group as attribute of Permission class

        Returns:

        """
        url = "/".join([str(fid), "groups", gid])
        return self.requester.post(url=url, data={"permissions": permissions})

    def set_quota_of_group_folder(self, fid, quota):
        """
        Set the quota for a folder in bytes

        Args:
            fid (int/str): group folder id
            quota (int/str): The new quota for the folder in bytes, user -3 for unlimited

        Returns:

        """
        url = "/".join([str(fid), "quota"])
        return self.requester.post(url, {"quota": quota})

    def rename_group_folder(self, fid, mountpoint):
        """
        Change the name of a folder

        Args:
            fid (int/str): group folder id
            mountpoint (str): The new name for the folder

        Returns:

        """
        url = "/".join([str(fid), "mountpoint"])
        return self.requester.post(url=url, data={"mountpoint": mountpoint})

    def enable_group_folder_advanced_permissions(self, fid):
        """
        Enable advanced permissions for group folder

        Args:
            fid (int/str): group folder id

        Returns:

        """
        url = "/".join([str(fid), "1"])
        return self.requester.post(url)

    def disable_group_folder_advanced_permissions(self, fid):
        """
        Disable advanced permissions for group folder

        Args:
            fid (int/str): group folder id

        Returns:

        """
        url = "/".join([str(fid), "0"])
        return self.requester.post(url)

    def add_group_folder_manage_group(self, fid, gid):
        """
        Add group to group folder manangers

        Args:
            fid (int/str): group folder id
            gid (str): group id

        Returns:

        """
        url = "/".join([str(fid), "manageACL"])
        return self.requester.post(url=url, data={'manageACL': 1, 'mappingId': gid, 'mappingType': 'group'})

    def remove_group_folder_manage_group(self, fid, gid):
        """
        Remove group from group folder manangers

        Args:
            fid (int/str): group folder id
            gid (str): group id

        Returns:

        """
        url = "/".join([str(fid), "manageACL"])
        return self.requester.post(url=url, data={'manageACL': 0, 'mappingId': gid, 'mappingType': 'group'})
        
    def add_group_folder_manage_user(self, fid, uid):
        """
        Add user to group folder manangers

        Args:
            fid (int/str): group folder id
            uid (str): group id

        Returns:

        """
        url = "/".join([str(fid), "manageACL"])
        return self.requester.post(url=url, data={'manageACL': 1, 'mappingId': uid, 'mappingType': 'user'})

    def remove_group_folder_manage_user(self, fid, uid):
        """
        Remove user from group folder manangers

        Args:
            fid (int/str): group folder id
            uid (str): group id

        Returns:

        """
        url = "/".join([str(fid), "manageACL"])
        return self.requester.post(url=url, data={'manageACL': 0, 'mappingId': uid, 'mappingType': 'user'})
