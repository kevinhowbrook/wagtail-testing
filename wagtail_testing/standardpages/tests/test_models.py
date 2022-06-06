from wagtail.tests.utils import WagtailPageTests

from wagtail_testing.home.models import HomePage
from wagtail_testing.standardpages.factories import (
    IndexPageFactory,
    InformationPageFactory,
)
from wagtail_testing.standardpages.models import IndexPage, InformationPage
from wagtail_testing.utils.models import PageRelatedPage


class StandrdPageTests(WagtailPageTests):
    def test_factories(self):
        InformationPageFactory()
        IndexPageFactory()

    def test_can_create_index_page_under_home_page(self):
        self.assertCanCreateAt(HomePage, IndexPage)

    def test_can_create_information_page_under_index_page(self):
        self.assertCanCreateAt(IndexPage, InformationPage)

    def test_related_pages(self):
        p1 = InformationPageFactory()
        p2 = InformationPageFactory()
        p3 = InformationPageFactory()
        p4 = InformationPageFactory()

        info_page = InformationPageFactory()
        info_page.page_related_pages = [
            PageRelatedPage(page=p1, sort_order=0),
            PageRelatedPage(page=p2, sort_order=3),
            PageRelatedPage(page=p3, sort_order=1),
            PageRelatedPage(page=p4, sort_order=2),
        ]
        info_page.save()
        info_page.refresh_from_db()

        self.assertEqual(list(info_page.related_pages), [p1, p3, p4, p2])
