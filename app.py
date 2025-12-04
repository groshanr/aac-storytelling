import gradio as gr
import time
# FIXME Prettify https://www.gradio.app/guides/theming-guide

# Modified from gradio documentation
def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.05)
        yield response[: i+1]

with gr.Blocks() as demo:
    with gr.Row():
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
        door = gr.Button("door")

        #btn.click(fn=update, inputs=inp, outputs=out)
    system_prompt = gr.Textbox("You are helpful AI.", label="System Prompt", visible=False)
    slider = gr.Slider(10, 100, visible=False)

    #FIXME. Review:
    # https://bibek-poudel.medium.com/create-your-own-chatbot-with-llama2-ollama-and-gradio-5c60ecb1aad0
    # main.py
    # https://www.gradio.app/guides/chatinterface-examples#lang-chain
    gr.ChatInterface(
        echo, additional_inputs=[system_prompt, slider],
    )
demo.launch(share=True)


# Possible interesting addition: https://openwebui.com/t/iamg30/story_element_generator_tool
# Verify I don't need https://docs.openwebui.com/features/pipelines/