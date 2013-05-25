# -*- coding: utf-8 -*-

from collections import namedtuple
import openaccess_epub.utils

identifer = namedtuple('Identifier', 'value, scheme')
creator = namedtuple('Creator', 'name, role, file_as')
contributor = namedtuple('Contributor', 'name, role, file_as')

#### Public Library of Science - PLoS ###
def plos_dc_identifier(article):
    """
    Given an Article class instance, this will return the DOI for the article.
    It returns a namedtuple which holds the value and scheme.
    """
    doi = article.get_doi()
    if doi:
        return identifier(doi, 'DOI')
    else:
        return None

def plos_dc_language(article):
    """
    Given an Article class instance, this will return the language in which
    that article was published. Since all PLoS articles are published in
    english, this will return 'en'.
    """
    return 'en'

def plos_dc_title(article):
    """
    Given an Article class instance, this will return a string representing
    the title of the article. This is done for PloS by serializing the text
    in the Article's
    """
    title_node = article.metadata.title.article_title
    title_string = openaccess_epub.utils.serialize_text(title_node)
    return title_string

def plos_dc_creator(article):
    """
    Given and Article class instance, this is responsible for returning the
    names for creators of the article. For our purposes, it is sufficient to
    list only the authors, returning their name, role=aut, and file-as name.

    This returns a list of Creator(name, role, file_as)
    """
    creator_list = []
    for contrib in article.metadata.contrib:
        if contrib.attrs['contrib-type'] == 'author':
            if contrib.collab:
                auth = utils.serializeText(contrib.collab[0])
                file_as = auth
            elif contrib.anonymous:
                auth = 'Anonymous'
                file_as = auth
            else:
                name = contrib.getName()[0]  # Work with only first name listed
                surname = name.surname
                given = name.given
                try:
                    gi = given[0]
                except (IndexError, TypeError):
                    auth = surname
                    file_as = surname
                else:
                    auth = ' '.join([given, surname])
                    file_as = ', '.join([surname, gi])
            new_creator = creator(name, 'aut', file_as)
            creator_list.append(new_creator)

def plos_dc_contributor(article):
    """
    Given and Article class instance, this is responsible for returning the
    names for contributors to the article. For our purposes, it is sufficient
    to list only the editors, returning their name, role=edt, and file-as name.

    This returns a list of Contributor(name, role, file_as)
    """
    contributor_list = []
    for contrib in ameta.contrib:
        if contrib.attrs['contrib-type'] == 'editor':
            if contrib.collab:
                editor_name = utils.serializeText(contrib.collab[0])
                file_as = editor_name
            else:
                name = contrib.getName()[0]
                try:
                    given_initial = name.given[0]
                except TypeError:
                    editor_name = name.surname
                    file_name = name.surname
                else:
                    editor_name = name.given + ' ' + name.surname
                    file_name = name.surname + ', ' + given_initial
            new_contributor = contributor(name, 'aut', file_as)
            contributor_list.append(new_contributor)

def plos_dc_publisher(article):
    """
    Given an Article class instance, this is responsible for returning a string
    for the name of the publisher. Since the publisher is already known, it
    just returns a string regardless of article content.
    """
    return 'Public Library of Science'

def plos_dc_description(article):
    """
    Given an Article class instance, this is responsible for returning an
    article description. For this method I have taken the approach of
    serializing the article's first abstract, if it has one. This results
    in 0 or 1 descriptions per article.
    """
    abstract_text = ''
    if article.metadata.abstract:
        abstract_text = utils.serialize_text(articlemetadata.abstract[0].node)
    return abstract_text
