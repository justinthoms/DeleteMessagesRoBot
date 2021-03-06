#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram.errors import (
    ChatAdminRequired,
    InviteHashExpired,
    InviteHashInvalid,
    UserAlreadyParticipant
)
from pyrogram.types import Message
from bot.bot import Bot


async def make_chat_user_join(
    client: Bot,
    chat_invite_link: str,
    user_id: int,
    message: Message
):
    try:
        await client.join_chat(chat_invite_link)
    except UserAlreadyParticipant:
        pass
    except (InviteHashExpired, InviteHashInvalid):
        return False
    await message.chat.promote_member(user_id, can_delete_messages=True)
    return True
