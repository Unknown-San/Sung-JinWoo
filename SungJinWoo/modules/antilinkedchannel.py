"""@Kaizuryu"""

import html

from telegram import Update, TelegramError
from telegram.ext import CallbackContext
from telegram.ext.filters import Filters
from SungJinWoo.modules.helper_funcs.chat_status import bot_admin, bot_can_delete

from SungJinWoo.modules.helper_funcs.decorators import SungJinWoocmd, SungJinWoomsg
from SungJinWoo.modules.helper_funcs.anonymous import user_admin, AdminPerms
import SungJinWoo.modules.sql.antilinkedchannel_sql as sql


@SungJinWoocmd(command="cleanlinked", group=112)
@bot_can_delete
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
def set_antilinkedchannel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            if sql.status_pin(chat.id):
                sql.disable_pin(chat.id)
                sql.enable_pin(chat.id)
                message.reply_html(
                    f"Enabled Linked channel post deletion and Disabled anti channel pin in {html.escape(chat.title)}"
                )

            else:
                sql.enable_linked(chat.id)
                message.reply_html(
                    f"Enabled linked channel post deletion in {html.escape(chat.title)}. Messages sent from the linked channel will be deleted."
                )

        elif s in ["off", "no"]:
            sql.disable_linked(chat.id)
            message.reply_html(
                f"Disabled linked channel post deletion in {html.escape(chat.title)}"
            )

        else:
            message.reply_text(f"Unrecognized arguments {s}")
        return
    message.reply_html(
        f"Linked channel post deletion is currently {sql.status_linked(chat.id)} in {html.escape(chat.title)}"
    )


@SungJinWoomsg(Filters.is_automatic_forward, group=111)
def eliminate_linked_channel_msg(update: Update, _: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    if not sql.status_linked(chat.id):
        return
    try:
        message.delete()
    except TelegramError:
        return

@SungJinWoocmd(command="antichannelpin", group=114)
@bot_admin
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
def set_antipinchannel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            if sql.status_linked(chat.id):
                sql.disable_linked(chat.id)
                sql.enable_pin(chat.id)
                message.reply_html(
                    f"Disabled Linked channel deletion and Enabled anti channel pin in {html.escape(chat.title)}"
                )

            else:
                sql.enable_pin(chat.id)
                message.reply_html(f"Enabled anti channel pin in {html.escape(chat.title)}")
        elif s in ["off", "no"]:
            sql.disable_pin(chat.id)
            message.reply_html(f"Disabled anti channel pin in {html.escape(chat.title)}")
        else:
            message.reply_text(f"Unrecognized arguments {s}")
        return
    message.reply_html(
        f"Linked channel message unpin is currently {sql.status_pin(chat.id)} in {html.escape(chat.title)}"
    )


@SungJinWoomsg(Filters.is_automatic_forward | Filters.status_update.pinned_message, group=113)
def eliminate_linked_channel_msg(update: Update, _: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    if not sql.status_pin(chat.id):
        return
    try:
        message.unpin()
    except TelegramError:
        return
