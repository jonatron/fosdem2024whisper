import json
import os

from files import files

### all one page
gen_html = "<table>"
for file_dict in files:
    filename = os.path.basename(file_dict['href']).replace(".webm", "")
    json_file_name = f"json/{filename}.json"
    # summary_file_name = "files/" + os.path.basename(file_dict['href']) + '.summary.txt'
    vtt_file_name = f"vtt/{filename}.vtt"
    # file_dict['summary'] = summary_file_name if os.path.exists(summary_file_name) else False
    file_dict['vtt'] = vtt_file_name if os.path.exists(vtt_file_name) else False
    try:
        js = json.load(open(json_file_name, 'r'))
    except Exception:
        continue
    gen_html += "<tr><td><b>" + file_dict['title'] + "</b></td></tr><tr><td>" + js['text'] + "</td></tr>"

gen_html += "</table>"

tpl = open('template.html', 'r').read()
out_html = tpl.replace("###", gen_html)

out_file = open('big.html', 'w')
out_file.write(out_html)


### links

gen_html = '''<a href="big.html">All text in one big file</a>
<br><a href="https://fosdem.org/2024/schedule/events/">FOSDEM 2024 Event Page</a>
<br>Videos are added regularly as they are added to the FOSDEM event page.
<br>Click "Play" for videos with subtitles.
<br>
<table>'''
for file_dict in files:
    filename = os.path.basename(file_dict['href']).replace(".webm", "")
    json_file_name = f"json/{filename}.json"
    txt_file_name = f"txt/{filename}.txt"
    docsrc = file_dict['href'].replace("https://video.fosdem.org/", "https://mirrors.dotsrc.org/fosdem/")
    try:
        js = json.load(open(json_file_name, 'r'))
    except Exception:
        continue

    summary = ''
    # if file_dict['summary']:
    #     summary = f'<a href="{file_dict["summary"]}">Summary</a> '

    vtt = ''
    if file_dict['vtt']:
        vtt = f' <a class="avtt" href="{file_dict["vtt"]}">WebVTT</a>'
    gen_html += f'''<tr>
      <td>
      <b>{file_dict['title']}</b>
      </td>
      <td>
        {summary}<a class="ajson" href="{json_file_name}">JSON</a> <a class="atxt" href="{txt_file_name}">txt</a>{vtt}
        <a class="avideo" href="{file_dict['href']}">Video</a> <a class="amirror" href="{docsrc}">Mirror&nbsp;Vid</a> <a href="#video_area" class="play">Play</a>
      </td>
      </tr>'''

gen_html += "</table>"

tpl = open('template.html', 'r').read()
out_html = tpl.replace("###", gen_html)

out_file = open('index.html', 'w')
out_file.write(out_html)
