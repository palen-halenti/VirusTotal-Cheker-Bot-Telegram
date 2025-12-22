from aiogram import Router, types
from aiogram.filters import Command
from assets.cheker import ip_checker, url_cheker, domain_checker
from aiogram.fsm.context import FSMContext
from assets.dialog import IPScan, URLScan, DOMAINScan
import asyncio

route=Router()

@route.message(Command('start'))
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='IP SCAN', callback_data='ip_scan')],
            [types.InlineKeyboardButton(text='FILE CHECK', callback_data='file_check')],
            [types.InlineKeyboardButton(text='URL CHECK', callback_data='url_check')],
            [types.InlineKeyboardButton(text='DOMAIN CHECK', callback_data='domain_check')],
            [types.InlineKeyboardButton(text='URL / FILE ANALYSIS', callback_data='urlfile_analysis')],
            [types.InlineKeyboardButton(text='ABOUT', callback_data='about')],
        ]
    )
    await message.answer(
        '👋 Welcome! This bot lets you check your files using the VirusTotal system 🛡️\n\n'
        'Please choose what interests you from the options below ⬇️',
        reply_markup=keyboard
    )

@route.callback_query(lambda c: c.data == 'about')
async def about(callback: types.CallbackQuery):
    about_text = (
        "👋 Hi! I'm Arkhyp, this bot helps you check IPs, URLs, and domains using VirusTotal API\n\n"
        "🌐 Check security reports: <a href='https://www.virustotal.com'>VirusTotal</a>\n"
        "💻 My projects: <a href='https://github.com/arhkypGitProject/ArkhypDanylov-Portfolio'>GitHub</a>\n\n"
        "⚠️ Informational only, not an antivirus!"
    )
    await callback.message.answer(
        about_text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )


@route.callback_query(lambda c: c.data == 'ip_scan')
async def ip_scan(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Send the IP for checking")
    await state.set_state(IPScan.waiting_for_ip)

@route.message(IPScan.waiting_for_ip)
async def process_ip(message: types.Message, state: FSMContext):
    ip = message.text.strip()

    await message.answer("🔍 Checking IP, please wait...")

    try:
        result = await asyncio.to_thread(ip_checker, ip)
    except Exception:
        await message.answer("❌ Error while checking IP")
        await state.clear()
        return

    if "error" in result:
        await message.answer("❌ IP report not found or API error")
        await state.clear()
        return

    text = (
        f"🌐 VirusTotal IP Report\n"
        f"IP: {result['ip']}\n"
        f"ASN: {result['asn']} ({result['as_owner']})\n"
        f"Country: {result['country']}\n\n"
        "⚡ Last Analysis:\n"
        f"- Malicious: {result['malicious']}\n"
        f"- Suspicious: {result['suspicious']}\n"
        f"- Harmless: {result['harmless']}\n"
        f"- Undetected: {result['undetected']}\n\n"
        "Source: VirusTotal.com\n"
        "⚠️ Informational only, not an antivirus!"
    )

    await message.answer(text)
    await state.clear()

@route.callback_query(lambda c: c.data == 'url_check')
async def url_scan(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Send the URL for checking")
    await state.set_state(URLScan.waiting_for_url)

@route.message(URLScan.waiting_for_url)
async def url_process(message: types.Message, state: FSMContext):
    url = message.text.strip()

    await message.answer("🔍 Checking URL, please wait...")

    try:
        result = await asyncio.to_thread(url_cheker, url)
    except Exception:
        await message.answer("❌ Error while checking URL")
        await state.clear()
        return

    if "error" in result:
        await message.answer("❌ URL report not found or API error")
        await state.clear()
        return

    text = (
        f"🌐 VirusTotal URL Report\n"
        f"URL: {result['url']}\n"
        f"Analysis ID: {result['id']}\n\n"
        "🧪 Analysis Status:\n"
        "The URL has been successfully submitted for analysis!\n\n"
        "🔗 Analysis Link:\n"
        f"{result['analysis_url']}\n\n"
        "Source: VirusTotal.com\n"
        "⚠️ Informational only, not an antivirus!"
    )

    await message.answer(text)
    await state.clear()

@route.callback_query(lambda c: c.data == 'domain_check')
async def domain_scan(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Send the DOMAIN for checking")
    await state.set_state(DOMAINScan.waiting_for_domain)

@route.message(DOMAINScan.waiting_for_domain)
async def domain_process(message: types.Message, state: FSMContext):
    domain = message.text.strip()

    await message.answer("🔍 Checking DOMAIN, please wait...")

    try:
        result = await asyncio.to_thread(domain_checker, domain)
    except Exception:
        await message.answer("❌ Error while checking DOMAIN")
        await state.clear()
        return

    if "error" in result:
        await message.answer("❌ DOMAIN report not found or API error")
        await state.clear()
        return

    text = (
        f"🌐 VirusTotal Domain Report\n"
        f"Domain: {result['domain']}\n"
        f"Registrar: {result.get('registrar', 'Unknown')}\n"
        f"Reputation: {result.get('reputation', 'Unknown')}\n"
        f"Total votes - Harmless: {result.get('total_votes', {}).get('harmless', 0)}, Malicious: {result.get('total_votes', {}).get('malicious', 0)}\n\n"
        "⚡ Last Analysis Stats:\n"
        f"- Malicious: {result.get('last_analysis_stats', {}).get('malicious', 0)}\n"
        f"- Suspicious: {result.get('last_analysis_stats', {}).get('suspicious', 0)}\n"
        f"- Harmless: {result.get('last_analysis_stats', {}).get('harmless', 0)}\n"
        f"- Undetected: {result.get('last_analysis_stats', {}).get('undetected', 0)}\n\n"
        "🔗 VirusTotal Link:\n"
        f"{result.get('url', 'N/A')}\n\n"
        "Source: VirusTotal.com\n"
        "⚠️ Informational only, not an antivirus!"
    )
    await message.answer(text)
    await state.clear()
