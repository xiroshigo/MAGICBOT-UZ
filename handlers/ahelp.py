from telethon import events, Button
import handlers.client
#part2
client = handlers.client.client
#bot
botClient = handlers.client.botClient
with client as darknet:
				darknet.add_event_handler(handlers.greetings.greeting)

@botClient.on(events.InlineQuery)
async def iquery(query):
			if query.text == 'ahelp':
							result = query.builder.article('Ahelp', text = "PLUGINLAR (ANIMATSIALAR) MENUSI\n~~INFORMATION~~\nMAGICBOT_UZ - 2021 YIL 22-MAYDA DASTURLANGAN\n2022-yil 5-avgust kuni mukammallashtirildi\nCreatorlar: @utc_creators\ndasturchi: @darknet_off1cial", buttons=[
							[Button.inline("uzbek sila", data=b"ctest"),Button.inline("lul", data=b"dtest")],
							[Button.inline("Tipratikan", data=b"rtest"), Button.inline("Loading", data=b"stext")],
							
							[Button.inline("Kiss", data=b"atest"), Button.inline("magic", data=b"btest")],
							
							[Button.inline("nikal", data=b"etest"),Button.inline("Dino", data=b"ftest")],
							
							[Button.inline("ketdim", data=b"gtest"), Button.inline("love", data=b"htest")],
							
							[Button.inline("police", data=b"itest"), Button.inline("fuck", data=b"jtest")],
							
							[Button.inline("what", data=b"ktest"), Button.inline("yes", data=b"ltest")],
							
							[Button.inline("ok", data=b"mtest"), Button.inline("no", data=b"ntest")],
							[Button.inline("Brain animation", data=b"otest"), Button.inline("Prank jokera 🤣", data=b"ptest")],
							[Button.inline("LOVE STORY WTF", data=b"qtest"), Button.inline("Naruto", data=b"rtest")],
							[Button.inline("SHARINGAN EYE", data=b"stest"), Button.inline("Tipratikan", data=b"ttest")],
							[Button.inline("Naruto jutsu", data=b"utest"), Button.inline("F TEXT", data=b"vtest")],
							[Button.url("MAGICBOT-UZ", url="https://t.me/Magicbot_uz"), Button.url("PLUGINS INFO", url="https://t.me/userbotcadr")]
											
							
							])
							await query.answer([result])
#callbackquery
@botClient.on(events.CallbackQuery)
#nq
async def callback(event):
				if event.data== b'atest':
								await event.answer("animation smilelar\nishlatish: .kiss", alert=True)
								#magic
				if event.data== b'btest':
								await event.answer("Yuraklar animatsiasi, bu animatsiadan sal ehtiyot boʻling floodwit rejimiga tushurib quyishi mumkun, kamroq foydalaning\nIshlatish: .magic", alert=True)
				if event.data== b'gtest':
								await event.answer("KETDIM DEGAN ANIMATSIA\nIshlatish: .ketdim", alert=True)
				if event.data== b'htest':
								await event.answer("Sevishganlar uchun chotki animatsia\nishlatish: .love ", alert=True)
								
				if event.data== b'ctest':
								await event.answer("kulish animatsiasi\nishga tushurish: .lul", alert=True)
								
				if event.data== b'dtest':
								await event.answer("uzbek sila animation soʻzi\nishgs tushurish: .uzb", alert=True)
				if event.data== b'etest':
								await event.answer("Nikal big text holos\ishga tushurish: .nikal", alert=True)
				if event.data== b'ftest':
								await event.answer("Dinozavrdan qoshayitgan bola animatsiasi\nishga tushurish: .dino", alert=True)
				if event.data== b'itest':
								await event.answer("Politsia signali animatsiasi\nishlatish: .police", alert=True)
				if event.data== b'jtest':
								await event.answer("FUCKYOU NEGATIVKAR UCHUN\nIshlatish: .fuck", alert=True)
				if event.data== b'ktest':
								await event.answer("NIMA big texti\nishlatish: .what", alert=True)
				if event.data== b'mtest':
								await event.answer("Ok big texti\nishlatish: .ok", alert=True)
				if event.data== b'ntest':
								await event.answer("No big texti\nishlatish: .no", alert=True)
				if event.data== b'ptest':
								await event.answer("Naruto animatsiasi\nishlatish: .naruto", alert=True)
				if event.data== b'otest':
								await event.answer("SSENI MIYYANG DEGAN ANIMATSIA\nishlatish: .brain", alert=True)
				if event.data== b'otest':
								await event.answer("Qizlarni buzib quygandagi holat 🤣\nishlatish: .sexstory", alert=True)
				if event.data== b'rtest':
								await event.answer("PRANK UCHUN SEN DAUNMISAN? DEGAN PRANK 🤣🤣\nishlatish: .pk", alert=True)
				if event.data== b'ttest':
								await event.answer("SSENI MIYYANG DEGAN ANIMATSIA\nishlatish: .brain", alert=True)
				if event.data== b'stest':
								await event.answer("anime Naruto Mangekyou Sharingan animatsiasi\nishlatish: .sharingan", alert=True)
				if event.data== b'utest':
								await event.answer("Narutoni clone jutsusi\nishlatish: .clonejutsu", alert=True)
				if event.data== b'vtest':
								await event.answer("F harfiga lyuboy emoji\nishlatish: .f emoji", alert=True)


								
											
																	
												
																				
								#ishga tushurish
@events.register(events.NewMessage(outgoing=True, pattern=r'\.ahelp'))

async def ahelphandler(event):
				results = await client.inline_query('@magicbot_uzbot', 'ahelp')
				await results[0].click(event.chat_id)
				await event.message.delete()
	