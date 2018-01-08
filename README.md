This dataset lists all the Media Types (MIME types), Media Subtypes, and their file extensions.

## Data

The details of the Media Types and Media Subtypes are taken from the [official registry of Media Types](http://www.iana.org/assignments/media-types/media-types.xhtml) maintained by IANA. The extension details are taken   [the website](http://svn.apache.org/viewvc/httpd/httpd/branches/2.2.x/docs/conf/mime.types?view=annotate) of the Apache Software Foundation.

## Preparation

The Type, Subtype, and Template name were copied from IANA's websites into a Google Sheets document. The link to the Template was generated in a fourth column in the same sheet by concatenating the Template name with a reference to the Template folder on IANA's website.

The extensions were copied from Apache's website into a separate sheet in the same Google Sheets document. The data was cleaned to place the extensions on their own in a single column without the Type and Subtype.

The extensions were finally added to the original sheet using VLOOKUP.


## License

These data are made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/