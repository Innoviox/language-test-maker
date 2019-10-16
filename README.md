## Language Test

Note: this project has tons of requirements. Install them with `pip install -r requirements.txt`.



There are three methods of translation implemented. The first one is `googletrans`, which is the most reliable; however, this has very strict quota and timing limits. Therefore, it is simpler to use the `duolingo` built-in translator, but this is not reliable and fails for several words (roughly 5%). For these, I implemented a headless-chrome variant option, which is reliable but slow.

