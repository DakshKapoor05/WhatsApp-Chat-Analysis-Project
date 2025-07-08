import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = r"C:\Users\PC\OneDrive\Desktop\wp-chat-analysis-app\download kara hua font\NotoEmoji-VariableFont_wght.ttf"
emoji_font = fm.FontProperties(fname=font_path)

# Check font name
print(emoji_font.get_name())