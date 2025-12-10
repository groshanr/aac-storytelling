# Modified from https://medium.com/@bonnyjames0830/a-comprehensive-guide-to-using-local-llms-offline-3bf63f6a400d
import gradio as gr
from openai import OpenAI

# Set up the local LM Studio endpoint
story = []

client = OpenAI(
    base_url = 'http://127.0.0.1:1234/v1', # or "http://172.20.20.20:1234/v1",
    api_key = "lm-studio"
)

def query_local_llm(user_input, story_text):
    """
    Sends a prompt to LM Studio’s local LLM and returns the response.
    Each query is treated as an independent session.
    """
    
    if not user_input.strip():
        return "Please enter a prompt."
    try:

        # Prompt template modified from @TheOdbball https://www.reddit.com/r/PromptEngineering/comments/1nt7x7v/after_1000_hours_of_prompt_engineering_i_found/
        response = client.responses.create(
            model = "allenai/olmo-2-1124-7b/olmo2_quantized_ft.gguf",
            input = [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": 
                            """
                                ///▙▖▙▖▞▞▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
                                ▛///▞ PRISM KERNEL ::
                                //▞▞〔Purpose · Rules · Identity · Structure · Motion〕
                                P:: write.a.story ∙ write.single.output  
                                R:: be.concise ∙ incorporate.story_text ∙ express.one.idea.only
                                I:: user_input ∙ story_text
                                S:: read.story_text → read.user_input → generate.sentence.using.both
                                M:: output: one.sentence  
                                :: ∎
                            """
                        }
                    ]
                },
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": story_text
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": user_input
                        }
                    ]
                }
            ],
            text={
                "format": {
                "type": "text"
                }
            }
        )
        return response.output_text
    
    except Exception as e:
        return f"Error: {str(e)}"

def clear_story_so_far():
    return ""

def clear_textboxes():
    """
    Clears both the input and output textboxes.
    """
    return "", ""

def create_prompt(input_text, value):
    """
    Combines text that is typed as well as entered via button clicks
    """
    return '{0} {1}'.format(input_text, value)

def story_so_far(story, output_text):
    """
    Combines accepted sentence with existing story
    """
    return '{0} {1}'.format(story, output_text)


# Create a Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# AACtive Storytelling")
    with gr.Row(scale=2):
        with gr.Group():
        
            radio_btn = gr.Radio(choices=['Adventure', 'Science Fiction', 'Mystery', 'Fantasy', 'Horror'], label='Choose a genre', show_label=True)
            @gr.render(inputs=[radio_btn], triggers=[radio_btn.select, radio_btn.change, radio_btn.input])
            def generate_aac_board(genre):
                button_list = []
                if genre == 'Adventure':
                    word_list = ['amulet', 'attempt', 'away', 'beast', 'canyon', 'captain', 'cave', 'chest', 'chosen', 'city', 'cliffs', 
                                'coast', 'community', 'curse', 'daring', 'deadly', 'door', 'dragon', 'elder', 'enchanted', 'explore', 'fear', 
                                'festival', 'forces', 'greed', 'guardian', 'house', 'island', 'key', 'lair', 'legends', 'live', 'man', 'map', 
                                'nature', 'pass', 'path', 'pirate', 'power', 'prize', 'prophecy', 'quickly', 'rainforest', 'relic', 'rule', 
                                'sea', 'seek', 'shade', 'shipwreck', 'staff', 'star', 'statue', 'storm', 'symbols', 'towns', 'treasures', 
                                'tunnels', 'vengeance', 'wealth', 'woman']
                    with gr.Row(scale=2):
                        for i, word in enumerate(word_list):
                            button_list.append(gr.Button(word))
        
            
                elif genre == 'Science Fiction':
                    word_list = ['ability', 'agent', 'artifact', 'brain', 'chamber', 'chance', 'city', 'colony', 'corrupt', 'cosmic', 'dark', 
                                'defeat', 'elysium', 'enigma', 'essence', 'explore', 'galactic', 'gateway', 'guardian', 'harmonizer', 
                                'homeworld', 'influence', 'interfere', 'justice', 'launch', 'leader', 'leap', 'legend', 'machine', 'message', 
                                'nebula', 'planet', 'prevent', 'project', 'psychic', 'quantum', 'realm', 'resource', 'restore', 'rift', 'rule', 
                            'search', 'self', 'shadow', 'ship', 'society', 'solution', 'surface', 'syndicate', 'tactic', 'teleportation', 
                            'thought', 'timeline', 'traitor', 'travel', 'truth', 'uncover', 'universe', 'voyager', 'world']
                    with gr.Row(scale=2):
                        for i, word in enumerate(word_list):
                            button_list.append(gr.Button(word))
                    
                    
                elif genre == 'Mystery':
                    word_list = ['abyss', 'amulet', 'artifact', 'beautiful', 'beloved', 'book', 'brief', 'case', 'change', 'chest', 'clue', 
                                'collector', 'confession', 'crypt', 'decade', 'decision', 'dimly', 'entity', 'estate', 'exit', 'figure', 
                                'friend', 'gems', 'gold', 'guise', 'heart', 'hill', 'house', 'labyrinth', 'library', 'location', 'locket', 
                                'lord', 'manor', 'mansion', 'map', 'monstrous', 'passage', 'person', 'previous', 'riddle', 'room', 'rumor', 
                                'scroll', 'shadow', 'share', 'silver', 'store', 'storm', 'suddenly', 'temple', 'theft', 'threaten', 'tragic', 
                                'trial', 'unknown', 'vanishing', 'wall', 'wealth', 'wisdom']
                    with gr.Row(scale=2):
                        for i, word in enumerate(word_list):
                            button_list.append(gr.Button(word))
                    
                    
                elif genre == 'Fantasy':
                    word_list = ['abyss', 'amulet', 'artifact', 'beast', 'book', 'celestial', 'chest', 'consume', 'cosmos', 'council', 
                                'curiosity', 'darkness', 'decision', 'destroy', 'dragon', 'element', 'embodiment', 'emerge', 'enchanted', 
                                'endless', 'energy', 'eternal', 'forest', 'glow', 'goblin', 'heart', 'hero', 'hold', 'hope', 'isle', 'king', 
                                'kingdom', 'lady', 'lair', 'lord', 'magical', 'past', 'path', 'plague', 'prince', 'princess', 'prosperity', 
                                'queen', 'realm', 'return', 'savior', 'sceptre', 'scorch', 'scroll', 'solve', 'spell', 'spire', 'stole', 
                                'sword', 'terrible', 'universe', 'villain', 'vow', 'whisper', 'world']
                    with gr.Row(scale=2):
                        for i, word in enumerate(word_list):
                            button_list.append(gr.Button(word))
                    
                    
                elif genre == 'Horror':
                    word_list = ['ancestor', 'artifact', 'beneath', 'book', 'cabin', 'carry', 'catacombs', 'cold', 'confront', 'consume', 
                                'creature', 'creek', 'cult', 'death', 'defeat', 'dormant', 'encounter', 'energy', 'engulf', 'entity', 'fall', 
                                'fear', 'figure', 'foggy', 'forest', 'hermit', 'hill', 'hollow', 'house', 'howl', 'imagination', 'incantation', 
                                'involve', 'knock', 'library', 'magic', 'mansion', 'mirror', 'missing', 'occult', 'ordinary', 'plead', 'protect', 
                                'recall', 'reclusive', 'remain', 'ritual', 'seen', 'send', 'shadow', 'smile', 'spirit', 'torment', 'townsfolk', 
                                'tree', 'village', 'warning', 'whisper', 'wicked', 'witch']
                    with gr.Row(scale=2):
                        for i, word in enumerate(word_list):
                            button_list.append(gr.Button(word))

                # Reference: #https://stackoverflow.com/questions/78536915/how-use-gradios-gr-button-click-so-that-it-passes-a-local-variable-that-is-no    
                button_list[0].click(lambda txt_value: create_prompt(txt_value, word_list[0]), inputs=[input_text], outputs=[input_text])
                button_list[1].click(lambda txt_value: create_prompt(txt_value, word_list[1]), inputs=[input_text], outputs=[input_text])
                button_list[2].click(lambda txt_value: create_prompt(txt_value, word_list[2]), inputs=[input_text], outputs=[input_text])
                button_list[3].click(lambda txt_value: create_prompt(txt_value, word_list[3]), inputs=[input_text], outputs=[input_text])
                button_list[4].click(lambda txt_value: create_prompt(txt_value, word_list[4]), inputs=[input_text], outputs=[input_text])
                button_list[5].click(lambda txt_value: create_prompt(txt_value, word_list[5]), inputs=[input_text], outputs=[input_text])
                button_list[6].click(lambda txt_value: create_prompt(txt_value, word_list[6]), inputs=[input_text], outputs=[input_text])
                button_list[7].click(lambda txt_value: create_prompt(txt_value, word_list[7]), inputs=[input_text], outputs=[input_text])
                button_list[8].click(lambda txt_value: create_prompt(txt_value, word_list[8]), inputs=[input_text], outputs=[input_text])
                button_list[9].click(lambda txt_value: create_prompt(txt_value, word_list[9]), inputs=[input_text], outputs=[input_text])
                button_list[10].click(lambda txt_value: create_prompt(txt_value, word_list[10]), inputs=[input_text], outputs=[input_text])
                button_list[11].click(lambda txt_value: create_prompt(txt_value, word_list[11]), inputs=[input_text], outputs=[input_text])
                button_list[12].click(lambda txt_value: create_prompt(txt_value, word_list[12]), inputs=[input_text], outputs=[input_text])
                button_list[13].click(lambda txt_value: create_prompt(txt_value, word_list[13]), inputs=[input_text], outputs=[input_text])
                button_list[14].click(lambda txt_value: create_prompt(txt_value, word_list[14]), inputs=[input_text], outputs=[input_text])
                button_list[15].click(lambda txt_value: create_prompt(txt_value, word_list[15]), inputs=[input_text], outputs=[input_text])
                button_list[16].click(lambda txt_value: create_prompt(txt_value, word_list[16]), inputs=[input_text], outputs=[input_text])
                button_list[17].click(lambda txt_value: create_prompt(txt_value, word_list[17]), inputs=[input_text], outputs=[input_text])
                button_list[18].click(lambda txt_value: create_prompt(txt_value, word_list[18]), inputs=[input_text], outputs=[input_text])
                button_list[19].click(lambda txt_value: create_prompt(txt_value, word_list[19]), inputs=[input_text], outputs=[input_text])
                button_list[20].click(lambda txt_value: create_prompt(txt_value, word_list[20]), inputs=[input_text], outputs=[input_text])
                button_list[21].click(lambda txt_value: create_prompt(txt_value, word_list[21]), inputs=[input_text], outputs=[input_text])
                button_list[22].click(lambda txt_value: create_prompt(txt_value, word_list[22]), inputs=[input_text], outputs=[input_text])
                button_list[23].click(lambda txt_value: create_prompt(txt_value, word_list[23]), inputs=[input_text], outputs=[input_text])
                button_list[24].click(lambda txt_value: create_prompt(txt_value, word_list[24]), inputs=[input_text], outputs=[input_text])
                button_list[25].click(lambda txt_value: create_prompt(txt_value, word_list[25]), inputs=[input_text], outputs=[input_text])
                button_list[26].click(lambda txt_value: create_prompt(txt_value, word_list[26]), inputs=[input_text], outputs=[input_text])
                button_list[27].click(lambda txt_value: create_prompt(txt_value, word_list[27]), inputs=[input_text], outputs=[input_text])
                button_list[28].click(lambda txt_value: create_prompt(txt_value, word_list[28]), inputs=[input_text], outputs=[input_text])
                button_list[29].click(lambda txt_value: create_prompt(txt_value, word_list[29]), inputs=[input_text], outputs=[input_text])
                button_list[30].click(lambda txt_value: create_prompt(txt_value, word_list[30]), inputs=[input_text], outputs=[input_text])
                button_list[31].click(lambda txt_value: create_prompt(txt_value, word_list[31]), inputs=[input_text], outputs=[input_text])
                button_list[32].click(lambda txt_value: create_prompt(txt_value, word_list[32]), inputs=[input_text], outputs=[input_text])
                button_list[33].click(lambda txt_value: create_prompt(txt_value, word_list[33]), inputs=[input_text], outputs=[input_text])
                button_list[34].click(lambda txt_value: create_prompt(txt_value, word_list[34]), inputs=[input_text], outputs=[input_text])
                button_list[35].click(lambda txt_value: create_prompt(txt_value, word_list[35]), inputs=[input_text], outputs=[input_text])
                button_list[36].click(lambda txt_value: create_prompt(txt_value, word_list[36]), inputs=[input_text], outputs=[input_text])
                button_list[37].click(lambda txt_value: create_prompt(txt_value, word_list[37]), inputs=[input_text], outputs=[input_text])
                button_list[38].click(lambda txt_value: create_prompt(txt_value, word_list[38]), inputs=[input_text], outputs=[input_text])
                button_list[39].click(lambda txt_value: create_prompt(txt_value, word_list[39]), inputs=[input_text], outputs=[input_text])
                button_list[40].click(lambda txt_value: create_prompt(txt_value, word_list[40]), inputs=[input_text], outputs=[input_text])
                button_list[41].click(lambda txt_value: create_prompt(txt_value, word_list[41]), inputs=[input_text], outputs=[input_text])
                button_list[42].click(lambda txt_value: create_prompt(txt_value, word_list[42]), inputs=[input_text], outputs=[input_text])
                button_list[43].click(lambda txt_value: create_prompt(txt_value, word_list[43]), inputs=[input_text], outputs=[input_text])
                button_list[44].click(lambda txt_value: create_prompt(txt_value, word_list[44]), inputs=[input_text], outputs=[input_text])
                button_list[45].click(lambda txt_value: create_prompt(txt_value, word_list[45]), inputs=[input_text], outputs=[input_text])
                button_list[46].click(lambda txt_value: create_prompt(txt_value, word_list[46]), inputs=[input_text], outputs=[input_text])
                button_list[47].click(lambda txt_value: create_prompt(txt_value, word_list[47]), inputs=[input_text], outputs=[input_text])
                button_list[48].click(lambda txt_value: create_prompt(txt_value, word_list[48]), inputs=[input_text], outputs=[input_text])
                button_list[49].click(lambda txt_value: create_prompt(txt_value, word_list[49]), inputs=[input_text], outputs=[input_text])
                button_list[50].click(lambda txt_value: create_prompt(txt_value, word_list[50]), inputs=[input_text], outputs=[input_text])
                button_list[51].click(lambda txt_value: create_prompt(txt_value, word_list[51]), inputs=[input_text], outputs=[input_text])
                button_list[52].click(lambda txt_value: create_prompt(txt_value, word_list[52]), inputs=[input_text], outputs=[input_text])
                button_list[53].click(lambda txt_value: create_prompt(txt_value, word_list[53]), inputs=[input_text], outputs=[input_text])
                button_list[54].click(lambda txt_value: create_prompt(txt_value, word_list[54]), inputs=[input_text], outputs=[input_text])
                button_list[55].click(lambda txt_value: create_prompt(txt_value, word_list[55]), inputs=[input_text], outputs=[input_text])
                button_list[56].click(lambda txt_value: create_prompt(txt_value, word_list[56]), inputs=[input_text], outputs=[input_text])
                button_list[57].click(lambda txt_value: create_prompt(txt_value, word_list[57]), inputs=[input_text], outputs=[input_text])
                button_list[58].click(lambda txt_value: create_prompt(txt_value, word_list[58]), inputs=[input_text], outputs=[input_text])
                button_list[59].click(lambda txt_value: create_prompt(txt_value, word_list[59]), inputs=[input_text], outputs=[input_text])  

        with gr.Column():
            with gr.Group():
                story_text = gr.Textbox(
                        lines = 24,
                        label="The Story So Far"
                ) 
                story_clear_btn = gr.Button("Start Over")
            

    with gr.Row():
        input_text = gr.Textbox(
            lines=5,
            label="Write Your Story",
            placeholder="Type your sentence here...",
            interactive = True
        )

        output_text = gr.Textbox(
            lines=5,
            label="LLM’s Suggestion",
            interactive = True,
        ) 

               
            
    with gr.Row():
        submit_btn = gr.Button("Generate", variant="primary")
        clear_btn = gr.Button("Clear")    
        retry_btn = gr.Button("Retry")    
        save_btn = gr.Button("Accept")
   
    submit_btn.click(
        fn=query_local_llm,
        inputs=[input_text, story_text],
        outputs=output_text
    )    

    clear_btn.click(
        fn=clear_textboxes,
        inputs=None,
        outputs=[input_text, output_text]
    )

    retry_btn.click(
        fn = query_local_llm,
        inputs=[input_text, story_text],
        outputs=output_text
    )

    save_btn.click(
        fn = story_so_far, 
        inputs = [story_text, output_text], 
        outputs=[story_text]
    )

    story_clear_btn.click(
        fn=clear_story_so_far,
        inputs=None,
        outputs=story_text
    )
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", share=True)