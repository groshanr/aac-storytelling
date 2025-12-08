# Modified from https://medium.com/@bonnyjames0830/a-comprehensive-guide-to-using-local-llms-offline-3bf63f6a400d
import gradio as gr
from openai import OpenAI

# Set up the local LM Studio endpoint
story = []
client = OpenAI(
    base_url = 'http://127.0.0.1:1234/v1', # or "http://172.20.20.20:1234/v1",
    api_key = "lm-studio"
)
def send_prompt(prompt):
    return f'Write a sentence using these words in order: {prompt}'

def query_local_llm(prompt):
    """
    Sends a prompt to LM Studio’s local LLM and returns the response.
    Each query is treated as an independent session.
    """
    if not prompt.strip():
        return "Please enter a prompt."
    try:
        # Always start a new conversation
        prompt = send_prompt(prompt)
        response = client.chat.completions.create(
            model="olmo-2-1124-7b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=50
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
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
    with gr.Group():
        with gr.Row():
            with gr.Row(scale=2):
                magic = gr.Button("magic")
                fight = gr.Button("fight")
                sword = gr.Button("sword")
                wand = gr.Button("wand")
                potion = gr.Button("potion")
                see = gr.Button("see")
                find = gr.Button("find")
                get = gr.Button("get")
                run = gr.Button("run")
                say = gr.Button("say")
                want = gr.Button("want")
                think = gr.Button("think")
                use = gr.Button("use")
                feel = gr.Button("feel")
                go = gr.Button("go")
                crown = gr.Button("crown")
                armor = gr.Button("armor")
                treasure = gr.Button("treasure")
                kingdom = gr.Button("kingdom")
                castle = gr.Button("castle")
                dragon = gr.Button("dragon")
                king = gr.Button("king")
                queen = gr.Button("queen")
                wizard = gr.Button("wizard")
                princess = gr.Button("princess")
                prince = gr.Button("prince")
                knight = gr.Button("knight")
                happy = gr.Button("happy")
                sad = gr.Button("sad")
                scared = gr.Button("scared")
                angry = gr.Button("angry")
                worried = gr.Button("worried")
                surprised = gr.Button("surprised")
                good = gr.Button("good")
                bad = gr.Button("bad")
                big = gr.Button("big")
                small = gr.Button("small")
                strong = gr.Button("strong")
                weak = gr.Button("weak")
                brave = gr.Button("brave")
                secret = gr.Button("secret")
                powerful = gr.Button("powerful")
                but = gr.Button("but")
                so = gr.Button("so")
                because = gr.Button("because")
                if_button = gr.Button("if")
                when_button = gr.Button("when")
                and_button = gr.Button("and")
                before = gr.Button("before")
                after = gr.Button("after")
                now = gr.Button("now")
                then = gr.Button("then")
                spirit = gr.Button("spirit")
                evil = gr.Button("evil")
                curse  = gr.Button("curse")
                bless = gr.Button("bless")
                loyal = gr.Button("loyal")
                love = gr.Button("love")
                hate = gr.Button("hate")
                fear = gr.Button("fear")

            with gr.Column():
                story_text = gr.Textbox(
                    lines = 16,
                    label="The Story So Far"
                )    
            
           
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
            interactive = True
        ) 
    
    with gr.Row():
        submit_btn = gr.Button("Generate", variant="primary")
        clear_btn = gr.Button("Clear")    
        retry_btn = gr.Button("Retry")    
        save_btn = gr.Button("Accept")
   
    # Reference: #https://stackoverflow.com/questions/78536915/how-use-gradios-gr-button-click-so-that-it-passes-a-local-variable-that-is-no
    magic.click(lambda txt_value: create_prompt(txt_value, 'magic'), inputs=[input_text], outputs=[input_text])
    fight.click(lambda txt_value: create_prompt(txt_value, 'fight'), inputs=[input_text], outputs=[input_text])
    sword.click(lambda txt_value: create_prompt(txt_value, 'sword'), inputs=[input_text], outputs=[input_text])
    wand.click(lambda txt_value: create_prompt(txt_value, 'wand'), inputs=[input_text], outputs=[input_text])
    potion.click(lambda txt_value: create_prompt(txt_value, 'potion'), inputs=[input_text], outputs=[input_text])
    see.click(lambda txt_value: create_prompt(txt_value, 'see'), inputs=[input_text], outputs=[input_text])
    find.click(lambda txt_value: create_prompt(txt_value, 'find'), inputs=[input_text], outputs=[input_text])
    get.click(lambda txt_value: create_prompt(txt_value, 'get'), inputs=[input_text], outputs=[input_text])
    run.click(lambda txt_value: create_prompt(txt_value, 'run'), inputs=[input_text], outputs=[input_text])
    say.click(lambda txt_value: create_prompt(txt_value, 'say'), inputs=[input_text], outputs=[input_text])
    want.click(lambda txt_value: create_prompt(txt_value, 'want'), inputs=[input_text], outputs=[input_text])
    think.click(lambda txt_value: create_prompt(txt_value, 'think'), inputs=[input_text], outputs=[input_text])
    use.click(lambda txt_value: create_prompt(txt_value, 'use'), inputs=[input_text], outputs=[input_text])
    feel.click(lambda txt_value: create_prompt(txt_value, 'feel'), inputs=[input_text], outputs=[input_text])
    go.click(lambda txt_value: create_prompt(txt_value, 'go'), inputs=[input_text], outputs=[input_text])
    crown.click(lambda txt_value: create_prompt(txt_value, 'crown'), inputs=[input_text], outputs=[input_text])
    armor.click(lambda txt_value: create_prompt(txt_value, 'armor'), inputs=[input_text], outputs=[input_text])
    treasure.click(lambda txt_value: create_prompt(txt_value, 'treasure'), inputs=[input_text], outputs=[input_text])
    kingdom.click(lambda txt_value: create_prompt(txt_value, 'kingdom'), inputs=[input_text], outputs=[input_text])
    castle.click(lambda txt_value: create_prompt(txt_value, 'castle'), inputs=[input_text], outputs=[input_text])
    dragon.click(lambda txt_value: create_prompt(txt_value, 'dragon'), inputs=[input_text], outputs=[input_text])
    king.click(lambda txt_value: create_prompt(txt_value, 'king'), inputs=[input_text], outputs=[input_text])
    queen.click(lambda txt_value: create_prompt(txt_value, 'queen'), inputs=[input_text], outputs=[input_text])
    wizard.click(lambda txt_value: create_prompt(txt_value, 'wizard'), inputs=[input_text], outputs=[input_text])
    princess.click(lambda txt_value: create_prompt(txt_value, 'princess'), inputs=[input_text], outputs=[input_text])
    prince.click(lambda txt_value: create_prompt(txt_value, 'prince'), inputs=[input_text], outputs=[input_text])
    knight.click(lambda txt_value: create_prompt(txt_value, 'knight'), inputs=[input_text], outputs=[input_text])
    happy.click(lambda txt_value: create_prompt(txt_value, 'happy'), inputs=[input_text], outputs=[input_text])
    sad.click(lambda txt_value: create_prompt(txt_value, 'sad'), inputs=[input_text], outputs=[input_text])
    scared.click(lambda txt_value: create_prompt(txt_value, 'scared'), inputs=[input_text], outputs=[input_text])
    angry.click(lambda txt_value: create_prompt(txt_value, 'angry'), inputs=[input_text], outputs=[input_text])
    worried.click(lambda txt_value: create_prompt(txt_value, 'worried'), inputs=[input_text], outputs=[input_text])
    surprised.click(lambda txt_value: create_prompt(txt_value, 'surprised'), inputs=[input_text], outputs=[input_text])
    good.click(lambda txt_value: create_prompt(txt_value, 'good'), inputs=[input_text], outputs=[input_text])
    bad.click(lambda txt_value: create_prompt(txt_value, 'bad'), inputs=[input_text], outputs=[input_text])
    big.click(lambda txt_value: create_prompt(txt_value, 'big'), inputs=[input_text], outputs=[input_text])
    small.click(lambda txt_value: create_prompt(txt_value, 'small'), inputs=[input_text], outputs=[input_text])
    strong.click(lambda txt_value: create_prompt(txt_value, 'strong'), inputs=[input_text], outputs=[input_text])
    weak.click(lambda txt_value: create_prompt(txt_value, 'weak'), inputs=[input_text], outputs=[input_text])
    brave.click(lambda txt_value: create_prompt(txt_value, 'brave'), inputs=[input_text], outputs=[input_text])
    secret.click(lambda txt_value: create_prompt(txt_value, 'secret'), inputs=[input_text], outputs=[input_text])
    powerful.click(lambda txt_value: create_prompt(txt_value, 'powerful'), inputs=[input_text], outputs=[input_text])
    but.click(lambda txt_value: create_prompt(txt_value, 'but'), inputs=[input_text], outputs=[input_text])
    so.click(lambda txt_value: create_prompt(txt_value, 'so'), inputs=[input_text], outputs=[input_text])
    because.click(lambda txt_value: create_prompt(txt_value, 'because'), inputs=[input_text], outputs=[input_text])
    if_button.click(lambda txt_value: create_prompt(txt_value, 'if'), inputs=[input_text], outputs=[input_text])
    when_button.click(lambda txt_value: create_prompt(txt_value, 'when'), inputs=[input_text], outputs=[input_text])
    and_button.click(lambda txt_value: create_prompt(txt_value, 'and'), inputs=[input_text], outputs=[input_text])
    before.click(lambda txt_value: create_prompt(txt_value, 'before'), inputs=[input_text], outputs=[input_text])
    after.click(lambda txt_value: create_prompt(txt_value, 'after'), inputs=[input_text], outputs=[input_text])
    now.click(lambda txt_value: create_prompt(txt_value, 'now'), inputs=[input_text], outputs=[input_text])
    then.click(lambda txt_value: create_prompt(txt_value, 'then'), inputs=[input_text], outputs=[input_text])
    spirit.click(lambda txt_value: create_prompt(txt_value, 'spirit'), inputs=[input_text], outputs=[input_text])
    evil.click(lambda txt_value: create_prompt(txt_value, 'evil'), inputs=[input_text], outputs=[input_text])
    curse.click(lambda txt_value: create_prompt(txt_value, 'curse'), inputs=[input_text], outputs=[input_text])
    bless.click(lambda txt_value: create_prompt(txt_value, 'bless'), inputs=[input_text], outputs=[input_text])
    loyal.click(lambda txt_value: create_prompt(txt_value, 'loyal'), inputs=[input_text], outputs=[input_text])
    love.click(lambda txt_value: create_prompt(txt_value, 'love'), inputs=[input_text], outputs=[input_text])
    hate.click(lambda txt_value: create_prompt(txt_value, 'hate'), inputs=[input_text], outputs=[input_text])
    fear.click(lambda txt_value: create_prompt(txt_value, 'fear'), inputs=[input_text], outputs=[input_text])

    submit_btn.click(
        fn=query_local_llm,
        inputs=input_text,
        outputs=output_text
    )    
    clear_btn.click(
        fn=clear_textboxes,
        inputs=None,
        outputs=[input_text, output_text]
    )

    retry_btn.click(
        fn = query_local_llm,
        inputs=input_text,
        outputs=output_text
    )
    save_btn.click(
        fn = story_so_far, 
        inputs = [story_text, output_text], 
        outputs=[story_text])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", share=True)