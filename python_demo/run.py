import ChatGLM

chip_number = 16
engine = ChatGLM.ChatGLM()
engine.init(chip_number)
engine.answer("你好")
engine.deinit()