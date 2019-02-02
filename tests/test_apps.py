from .base import BaseTestCase


class TestApps(BaseTestCase):

    def test_get_enable_disable(self):
        res = self.nxc.get_apps()
        assert res['ocs']['meta']['statuscode'] == self.SUCCESS_CODE
        apps_list = res['ocs']['data']['apps']
        assert len(apps_list) > 0

        # app to edit
        app = apps_list[0]

        # disable app
        res = self.nxc.disable_app(app)
        assert res['ocs']['meta']['statuscode'] == self.SUCCESS_CODE
        enabled_apps_list = self.nxc.get_apps(filter="enabled")['ocs']['data']['apps']
        assert app not in enabled_apps_list
        disabled_apps_list = self.nxc.get_apps(filter="disabled")['ocs']['data']['apps'].values()
        assert app in disabled_apps_list

        # enable app
        res = self.nxc.enable_app(app)
        assert res['ocs']['meta']['statuscode'] == self.SUCCESS_CODE
        enabled_apps_list = self.nxc.get_apps(filter="enabled")['ocs']['data']['apps']
        assert app in enabled_apps_list
        disabled_apps_list = self.nxc.get_apps(filter="disabled")['ocs']['data']['apps'].values()
        assert app not in disabled_apps_list

        # get app
        res = self.nxc.get_app(app)
        assert res['ocs']['meta']['statuscode'] == self.SUCCESS_CODE
        assert res['ocs']['data']['id'] == app
