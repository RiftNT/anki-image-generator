# anki-image-generator
This Anki addon retrieves input a word or phrase from an Anki note, 
then searches the web for an image related to the input and displays 
the image in a specified field of a note. The addon uses web scraping 
techniques to search and retrieve the images and can be used to update 
a whole deck or a selection of notes. It is a convenient tool for quickly 
adding images to multiple notes in bulk.

## Config Options
* `card_selection` - 'override' if you want all images of the selected deck to be changed
* `deck_target` - the target deck you want to generate images on.
* `key_field` - the field to be used as input for searching the image
* `image_field` - the field to output the image

## Notes
* ***restart* Anki after changing configurations**
