# Anki Addon: Image Generator
This Anki addon allows you to generate images and place them in a specified field of your Anki notes. The images are generated based on a search query, which is taken from another specified field of the notes.

## Configuration
Before using the addon, you need to configure the following settings in the addon configuration menu:

* `card_selection`: This setting determines how the addon selects which notes to change. You can choose to either 'override' all notes, or only change the notes with empty image_field.
* `deck_target`: This setting specifies the deck in which the addon will operate. You can either enter the name of the deck, or use a tag to specify the notes.
* `key_field`: This setting specifies the field of the notes that will be used as the search query for generating the images.
* `image_field`: This setting specifies the field of the notes that the generated images will be placed in.

## Usage
To use the addon, simply go to the Tools menu and click on the "Generate Images" option. The addon will then generate and place the images in the specified field of the selected notes.

## Notes
* The addon uses Bing's image search service to generate the images.
* The addon will try up to 5 times to find a valid image for each note. If it is unsuccessful, the image field will remain unchanged.
* The addon will show a notification with the number of changed notes after it finishes running.
