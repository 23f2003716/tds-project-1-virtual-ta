# GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/1

## Topic Metadata
- **ID**: 163247
- **Slug**: ga3-large-language-models-discussion-thread-tds-jan-2025
- **Created**: 2025-01-14T13:00:03.125Z
- **Views**: 1060
- **Replies**: 75
- **Likes**: 40
- **Tags**: announcement, term1-2025, graded-assignment, week-3

## Original Post
**Author**: Anand S
**Posted**: 2025-01-14T13:00:03.324Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/1

Please post any questions related to [Graded Assignment 3 - Large Language Models](https://exam.sanand.workers.dev/tds-2025-01-ga3).

Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. See below code for example

ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms

Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through Discourse Docs!  :slight_smile: 

Deadline: Sunday, February 2, 2025 6:29 PM

@carlton @Jivraj @Saransh_Saini

---

## Reply 1
**Author**: Anand S
**Posted**: 2025-01-14T13:06:47.583Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/2

*No content*

---

## Reply 2
**Author**: Nilay Chugh
**Posted**: 2025-01-15T12:20:05.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/3

how to get the dummy API key?

---

## Reply 3
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-15T14:59:06.607Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/4

Hi Nilay,

In order to make a api call to openai chat completions you are required to send authentication information(openai key) in headers. For first question of GA3 you don’t have to send actual(working) api key, any dummy api key would work(you can put your name, or tds anything works)

kind regards

---

## Reply 4
**Author**: Nilay Chugh
**Posted**: 2025-01-18T04:43:01.431Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/6

which API should i use in 7th question

---

## Reply 5
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-01-19T07:36:55.428Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/7

need help in question 4th. how can i correct this json body? sir  @Jivraj

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Extract text from this image."
    },
    {
      "role": "user",
      "content": {
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}

error:The JSON body must have 1 message

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": {
        "text": "Extract text from this image.",
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}

Error: The message must have a 2 content parts

---

## Reply 6
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-01-19T16:53:34.970Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/8

@Jivraj @carlton  sir plz see it once.

---

## Reply 7
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-21T07:02:52.278Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/9

Hi @22f3001315 ,

You are almost correct, there are very minor changes that needs to be made.

Take help from Chat GPT or use this documentation which have correct json body [Vision - OpenAI API](https://platform.openai.com/docs/guides/vision).

Kind regards

Jivraj

---

## Reply 8
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-01-21T08:21:45.804Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/10

it worked thanks sir

---

## Reply 9
**Author**: Muhammed Adhil Pt
**Posted**: 2025-01-21T11:25:57.882Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/12

Are we supposed to buy open ai api key ?

---

## Reply 10
**Author**: Sakthivel S
**Posted**: 2025-01-21T12:01:17.870Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/13

No, if you scroll down to the last question, we can get our Ai Proxy key

---

## Reply 11
**Author**: Carlton D'Silva
**Posted**: 2025-01-21T12:06:09.235Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/14

@nilaychugh @22f3002034

The API key is available at [https://aiproxy.sanand.workers.dev/](https://aiproxy.sanand.workers.dev/)

The instructions on how to use the token is given at [GitHub - sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

You cannot use this token directly with Open AI or any other gpt. These are only valid via the API exposed by the above instructions.

You get a limit of $1. Use with care.

Kind regards

---

## Reply 12
**Author**: Nilay Chugh
**Posted**: 2025-01-21T14:30:30.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/15

but the embedding model that is said to be used is text embedding 3 small, which is the model of OpenAI

---

## Reply 13
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-22T09:13:43.408Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/16

Hi Nilay,

Yes you would need to use `text-embedding-3-small` model of openai for embedding questions.

Kind regards

Jivraj

---

## Reply 14
**Author**: Nilay Chugh
**Posted**: 2025-01-23T03:52:39.679Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/17

i have a doubt, while submitting the GA3, both 7th and 8th questions require the API url to be active and connected right, but its not possible as both the URLs use same port, so if we check my 7th question URL is running right now, it’ll show as correct, but then if i  run 8th question URL, the 7th question will automatically show the error, **is there any solution to this problem?**

---

## Reply 15
**Author**: VIKASH PRASAD
**Posted**: 2025-01-23T06:09:55.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/18

Q5.  How to handle the error ? sir @Jivraj

Error: The first input does not match the first text exactly

---

## Reply 16
**Author**: VIKASH PRASAD
**Posted**: 2025-01-23T06:17:12.711Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/19

Q4. How to handle this error? @Jivraj

{
  "id": "chatcmpl-AshDCPwSiXNao1QXmCxCmi63GifFx",
  "object": "chat.completion",
  "created": 1737599182,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The image contains an email address and a number. The email address appears to be associated with an educational institution, and the number seems to be a numerical sequence.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 592,
    "completion_tokens": 33,
    "total_tokens": 625,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.05490624000000001,
  "cost": 0.001974,
  "monthlyRequests": 14,
  "costError": "crypto.createHash is not a function"
}

Error: Model must be gpt-4o-mini

---

## Reply 17
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-23T10:58:14.611Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/20

Hi Nilay,

 nilaychugh:

both the URLs use same port,

You can run two servers on different port numbers.

---

## Reply 18
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-23T11:05:13.578Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/21

Hi Vikash,

I looked at your answers in backend. In answer you submitted response from openai, but you need to submit json object which is required for sending a request to LLM.

Kind regards

---

## Reply 19
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-23T11:07:22.861Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/22

You made same mistake here, instead of response use json body that’s required for sending request to LLM.

Kind regards

---

## Reply 20
**Author**: VIKASH PRASAD
**Posted**: 2025-01-24T01:17:21.325Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/23

Q4. how to handle this error ? @Jivraj

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image"},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,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DOYQc83d7la67bar84q8XbP//qXbYYfS9YuJSdsaR+6nbLvsUsfWGWeU7n3vK93225du881L96Uvla4X6JP3+8X35P173KPeW77mwd12K92mm5bujW+sfVQ5+kX/ZNzvumvp+kXOanZa6KVeyqz8/cJ1UrfpuSOvvPLKK691+1rWM/UiPyLDokEPe1gp1752jYaJdvVOr/QOYhKV6x3UJDLXcGSlF9mld7aTiJBt38XSO9FJtEz02fa3yNdVrlLKXe5Sj9/YdhYNl6fImoi6yOed7lSjaragHaF46ENrNPl736vpeyFQeqc62SoXLRX9Ug/b7I78qIfomyi9yJ4ovnv2AmGSv8iX4yreEzkUlWcX+ftpK7t3ymdxm9vU4wei3yKM8h2D3dRZBE19+4VAudKV5j6cws6E6NxrXlMjbHe9a42GDukFwCTiLwpnO/+Rj6z2m4a9eqFUHve4GiV0nTqHsNIwLh05GY4P85D5qBfNk503O12i24udr0S8Rfnt8Pnc+DVOhuPctXZS+gXAJK37iNr3Yn0SDfe5a8whyvTyl9fovflDeey63fe+9ViOeUC+5gjjWEReOaVXN0d6+oXI5IiifO3APeQh9SiiHZ42j4q2mx/tNngtFrsadvfa/BlCCGHlsayintPYaqtSXvjCKlL9bbvYNjBnw7FxVqedVtOffnp1UEccUR3btttWB0hoNzgmDorod/SmHV0hwglbju/JTy7lEY+o29TuxcnJ2zEZIrhfzUxenKb3CFvHcjhc5eNELQo4T+WwnW3r3Ra1ow62vpVb3u5BuMuLo1W+612vlMMPr2W3pS5PL+J+ww3rVj+RrlzS7r9/KQ96UCkbbDBXyR5pLDIc/yEglHcM2/e22ZV1111XCYsx1IN9iZeddqr3bmdnm+0//ekqMHbeuQp/9T7wwCqGHvCAUp71rGpzP9lfWmW3SCF2iBcor8WLYwy77VbbcvvtSzn44LpAmsYC69BDa7r2evSj63GZ1j/mQ7scdVQVQO1aYu3446sAme4vjj886lHVbur8speVcthhdRFKgEE9LG4II/3KZyCKCCj97V73qvfae+9a91ZONhu7FmxicaiPKt+pp859MIdjF45GPP7xtW21i2MXjlYcdFA9EmI8WZgph7zYyZERotHRiPZyf+Vj95afoxePfeyq9w85ZLw9xrC4bNe213xt5OjW0562elrtq50XwnEx41+/MUbYUtt4ObalTs3uyqJMC6Fc2t9PR66MqXZsxRxk3PvM+DUeFztf6d/6iv7gPXm6vo1z48rv0krX5hpzh3HXjtm4Rpkc29IOhLr5x1jW3p6XaMd3zC3mr+E8Zn6wgND/CX5HieTrM31Hfvqca5uodz3RP9/ifxpjQV/Tl9ne8TJ1DiGEsLJYVlHPGTkHL8rF2XBk4OQ4GmfGOTUOszlEYtZDY/e7XxVpm2xSP2tIw4FyLAQzp8ZRtocTPUjGeXsgtjkeTkmEWlRLtN79lIFgUA738B7nDfcj1t2LYCS0CDNOUiRs+KCcazhlzlNaAlxd1Vndm0NuTpZzJ8DV02fSivIpd7MPiAH3JGzUq5Wt0fIjnkTRXG9xMXyAboh7ijI6+21hoXzKLV+24Ojf//5ab0JCPe2YEFgi8OrC5kTo0UdXgWyXQfmJCiLGYoEN5EdME5DOGhMgoqSi/4SldC3ap1z+lp/yeaDZboj2VC9nkO0EjEGkiDq6lqi2KHIO3Yvd7LQQulCf1l/U20JOXdXbGWiipQkl6BfKqvzq7zNt7D6veEUVioRRE2juxTauZ1PiyaLBQ976HdhFHsokgqt9p8WRPCwOTzqpplVH/Zewt6ukzbWfxZvyq7O+ThQaT6477rgqEKXRL/QlC9/nPa/2F3291Z8oVkcR6vlgC7s20unf2tJuludcjCsLGG3U+qR0Fk7spx21p3bVvtpKe2v3MfQftlFfadhd21joEJXq6+FsY14aD74ulB+bqz/srjVBD+1EgPtbG7nXYucr+fhpPtFmzrprp9af7Q5oO23FLvKWj/HJ7kPkpSzKYE7yN7sZh8rRxr4Ag0URG+h78jKHsK3FiPZWH5hntIm5ysJF/zAmTjml9me2tBCwYH/mM2sQwnhvtmqojznDolHed7zjqnkjhBDCymKdTM0cJOdiK5fT4SQ4Sy/C8eEPr9FfInAazoQwI/qJWMLiVreqkUjOvgluDpRgI3I8HHfyydVJE6AEtc8JL05rTDQ3iE+OlkPk/Dny4SKjwRnKT7ox3I8A5SA5eM5eecYEODheolkdphc2aPk5eqMOdijYcb4IGsFBkBIfRIv7twWH9iDqCFAC0fEiAobdiFW7E/vuW23M5u5JNBAn7klMEIneUyb5EZUiq8opIvz0p9fjVBZsRE6LUBOBbOKBXJHRJzyhlAMOqLsXorHaWtnHIJqUm7Bzn913r9d66T92Gghn7T3sL+qz5561rzUbLAZ9lhhiE2V74hNrOXfYod5fO/ipjxCH2o0gtUPiM3W1GCD2iVL3bzsli6H1P/cm4kSOLWDtOrA/MciuyunoyB57VJvbMXJvwlh97bh4qNcRE+lFx+0AjKE++v+xx1Zb+vYdbcnG8mjC3g6Pe0hL0HuPndlHWuVQVvezWGmLp8Xi3sruOJg87Y6oozFibE+L0YZxzS4gmqVr91Y3fdV7ym38jjE2X8lT/3ckRzvq7xZO+qIdGPkpH3Gu3QhiZbEoMqaHtLnDZ2yjrzT8bnGkzzW7EvsWa8MdzIZFkYWbxZoFsQWYhafoP9tbMEpjgaVvmhOIfw/1u0b+2rFh7Km3+ulzw0BFCCGElcVaF/WEGMFIBHAwhIlI01LDMYmwO3bhRbRwhCJfWFNRcW4gHjht4kM0jHi1ABmjRfUILY6XqCWyh1F8EALEofyIVs57IUT42oJi+isQLVx8RvQQLJy2Yyki7Y7d3PnOVSC3+xAJ/hb5JGwsJGzlq6O8vERbCQHnhS04iCAihLiWh7zANu5L8MhHvbyUzxEERzh8Ld8YbOWe8kATR953jWvloT7zLZ4Wizy1h+iw9iBu2YooJ9we/OAquN3HAsxn2li/s/Book0U14sQFG1datTVIsvCTfvoP+5jgczu2tI4kE4E1/izEG07J9MYRwS1xYh2VCdj2N/qs8EGta2IP3UUTbbDQux7ZqPZ3i6JRcZznzven88OZXe8RF3Y109214+ITm0/hn7HDq5x9MqiU9rWd5SXAB8K6SELzVf6q98tIPVfR9Ie85gaAbegsdNo8ewzgQP9g21E8dlVGdzXom++nRLjlaD3HWWOXLG5IIb6uH4aQt3xIceq1E2bidIbI+5p0WAOFDix42QR4nkYX5Np0WDMW5zDNeYX41h/dmRvbCERQghhZbDWRT0BZ3vemV/HTmzniv4sNZw5B+wr4Wwdc7icuLP2RNV8ImA5ECHjbJ/97BrpI6xEVsdQLpGzY46pDn/4UN0Qzl69iDbHTaRZCCJbxFFaAmkoqggF0TtlIvTYSUSf2CPiiIJp3M9r+igB5Ee8EK6OvVjEgLgjgomKJuqVw1EOP50bJ4rUfzHtwyai4QSHo0Oit6LR7r/UsDfxBxFndm+7Ik04EjwEHNiM7diQLYlg12sHNiAG2wJzKSGiCWj9TPnYSBt5z8vv031pIYbjyHl2ZRYBFqG26+LYRjsnTzRaaFoEELBstFSwp3Y+J7C1OYb4F03XN40tUWnC1oKEeB9jofmKQHbW3y4E0e6IksW45wHsEJpzPGuiT4iU2wUzzpTBYk8Z7MjZpfIaQ5+yE+TYkp20Bz6wPptA4Lt2Gg+wv/SldRFiceEolgdwLdIt9ux0WCRYYLV6aCtty04WLuxE0LOLCD48Y6MOrX+HEEJYeazVKZpD42Q4KOdsHefg6NZEZCwWApJQJEKImfZPgTh0zpHIWhtwjBy7h96IEg9YEgZjkUpiqIkBDpQjteUt7TDSTDwpv4WCuhG280XQOGf5ijBzyKLshN3QORPBdjUIemJQekcEiHKvsbzdd75jS/ITeWxt0NIMRX07JqXtRY7322/Vt4v43WJGpJMw0W/GkC8x7Rt47AAoN5FJBC32wczFQtRrS/doRykaTdQTsa1d1Y+tRUqJLyJOlJioJ5JFcImppYaNifmhzf3uvfb+sC+dHdJaYIniWnDpk2ysrs5jayNiESLH0upfRLgFxlLR6nBOIF7t3NhN8W01Htx2JMzC2ZEsR6G04TQLzVcWvo7+eEhY/7UjpV2NIefsjXELOs9P6DNwT/ayGCCu7YI5z07cE+NjsL9+YkeE6LYgN49ZQOjb08f92Ny4VGeLdFF9Y98xG4v6tsCzqG7zLtsak+YnacwFxrC6+9vc6dX6VAghhJXJWpmmRcEIGs6Rk+NAOFaCZymjeQvBmRFeytIidZwlx2a7uR3hmEb5CBRitG3Zu3YaokB+0jWIQFE+W9quEWXz9ZdExDTK4Ky6aDXnSeCK6HPA0xBORD2x2JzxfIKnRdw4amXk7KfTsondBAJBehFl5VH3FvGFzzh5RzUIB3bxXotGW4goj/Tt2MUQ9pPeoqRFRtVV2zgSpE846+65B+JJnkSYb3hh9+njBvInsIkotnW23GKAAFFn/5RMVFTfmy8Su1iUU19pQmiIcqmTNlY/tAUlsSfaS8yLDIuEEoj6wFheKw3trR30YTa1yHOsxvMLbN0WiUPYwqvZYl3TFlieJbD40yb6jF0rwlc76OttkbWY+UpbE+tebEJwtwUsexDexoDFHLuxhV2re96zHtch+u34KIcyGOcWz0OxPU0rp7QWHMbh2FwE5ZCfRYZFhD443+6XcdTGrHKaC4x/wQgLAs+RvOhFNdhgke04jv7MPhYX+kgIIYR1Tz/1Ly+cuzOpviGDyOJoOFZnkpcykgfOmBNqD3YN8Rnnwwly3u7doomEFtHYRIg0ItXEGgfq/LgjJJy2fDm9hmsIAM5YWk7Xe663I+DMqs/vf/8qgsYEPWFg296DagSUs6uEk2juGKLGnC4nLT9iej6URVrCW33HvsaOQ7cYIT7kqf5s5Rrt18S06J3yOQOsvsQLu4kYsqFzzhYN2lj01mcERRMT8pGnBcnQhnB/58A9kNsewvT1edIRF+rQ2mcaYodAI+pd274ilLAhyuwaLCTqfaaM7NpgA3+36ywe2JlAbAKp2UU672nz4X0soog2NvQNO55bYA+iXlvMAq3NiVNieJ996gPCO+5Yx446a1O0qLI205dcuxLQX0XVtelee9UHffURUfM2J7RxtCbzlfrqe8PdqIZ5QJ+Wd+tbdtbYxqJVP/WyODJWzAF+WkAYN47LeOCVfYf9Xn7sqj/qX2xv/DkSZVwpf0P/lJfxLb3fHY/ybI/+2vKVrs2P6miu857x7OV+Iv3Kb37Vh41Hxxg9QLzQ2AohhLD2WFZRzzFw7iLQHtzi6Iit+R58PDe4F8fpmyc8GGvr2N/e9xJ9Ft3iFAlP4kO0mTD1MBjhwnm1MhNhHLa0HD4RRrQT3y3S38S7+smrfTWm+3LKRx5Z0xIFHkxrkcCGe3HCHKZvF3FP2/IEk3vNh/w5VWXndN17PpSRAycALE7GRL1yyQfqpa5exJD7KKP3OfAPfKC+5xpCwTdziKT73TEEtvKZCGETU8SGuiqL37UDu8H7xIYyEgvSEEiEhUWQBw6JBmKoiZCGa9nCtS1qSWgRJo7f+K5x9Za/tGO4F9GlzYk593Kf1l+aeJcPweWnRaOFWvtM2TyUSGANBY7+I4qrLj4niByj0E/a8aOVDptqFwJV2VtUXj3tFBk7+ri/iUf9iMjVzmzU7M6m8tFWC7XHcuCrQJ1997CpMuvPyquMxp720U5E/WLnqybo2Uc/0V/UUb3kr64+t4tmLOkjL35xnZssUltflo4oZysLQDa2q+ZcvIWHOUE/g3u5jzFnASBfY9FulmeFHN2zOFAG+bOzxZgFuHyNR/+TwTMAnltpizG28Jn+r7wWyNrRcwR2aAQmvHwbljp4VsSOo/+1MDavhRBCWDcsq6gnkjkP34/tLKgzuf5L6nLAyRIezqYSdR48aw9cEn4ctW1kW92cFodNhHKknJ8HzzhLZRbN8nWMyupbPKS1de5IDFEv+kukcagcqXx9u4gtfveTj/PGxI0z9KL0Y3DSnC5Hy+l7eM15cNHBhVBGjn/6HPcY7iFSzSbE/3S0EcSB4wJEO4Hib8cJOHnHhwgO9RW59BAgsSIvAk2E0I6ECKg29pkytaMNbMP22qDZmX3VF+ri4VaixNGjJvbhOvclYLyIxiFsrY0JC31s+OAg4W33gKAhopVrDCKVKCGGlIsgUwb1JpaGaF/f3CLiTuAQs62/tDYcYsFAKDpK5DPlcT3hZHEwCyhnE6UivO0ZhWFb6jMEsr7WznyL4rIR4Uhksqn21c7L9TDzfLQHZQl4At8CUN/1MKnjWQSqcY7FzlcWZfq3z80B+os6Dsc0uzhmY5x66QdEufnD4oHw9rC7B1cJa4sHc5iz+YSzvNp/mfW5seBac5C5yJykXo6bWbBrD0e8XGduMi49QG5uMh7ZwX+dNc4tzi3I5Gt8+1YibcgO7h9CCGH2WK/rmft9EfTKeQ0QZXrDG2rUidDjLPwcQlQ5Z8rZTEcvOcfXva5Gi4hkW+BEWkMkiUPkiGxlE8McNjEoeuzcZzuaQvj63mgPq3HGxC2HRhwTnhyiaLN0nK3rfGe6a4g+olRa50g5YqJEWqLFeXDRdc6TM/VQoQdj5e8IzXTUXTmdp3WNHQULCE5+LK36Ki/hqkyELbu+5CVVOD3lKasi0mOwB5FCiLbzvNPCXt0cK3KswjeaOB5ABNv1IFZEMkXuCGvv+8YQEXnlZXvCxjeDKCshq0exi+167WcXRPmU3U92lNYRI8KJGNfGBBdx3epCzIjU2+kgSlzviJKytvPJ7K2tiR35tKiha9nNER7PJsiTGGJrP4k2AlP7+opBAt5xh7Z4sNNA4BNGIqZsou/qk+4ncqkd9QE2IcYsJP2XUw+TNpEI546NAYsrx4vsQLhWm/uaRcLL4s/iQx2UxcsCynvsQiCzo68rZHvv6TvKYrHhzDdR5l5EnXR2ZZTNrpGxAg97WlhIY1HiIWNplNlXRmob56c9YOklwmtx51tQ2vlp/dAi2thlK7sxFnmi4USm9pHWOJFeGrbUjyyijUF2VvbWli0art4Ep3uwu8WDcehevqFFP4N89S12sTg3P8h/DAsSbUzAa2NtpY+ab/R3/VAZlGVN5ivzhbpb7LKxvsuW7qeNzFe+KrKNafmbGyyEzQ36pHmEgCfS1U2ZlE1gwNgzBo1X+Rqn6ihw0fLV/7S7er3ylXWh6z35e1lUSMtGymtctP5rblAffYE9jTMP5hvr2mwabehBdu2hb3n+pbVHCCGEdc/6z+iZ+30R9J5zDeCEOCNb2y1SxBkMX8QTAeQnZzQNB+w6IpjAGDobwsJ1RI17EJTSi4o5KiE/ESwvQqaJT++7VnpOlMDg8OSvTMQgIShti5qrByEqL2mJGPcWfSNIiC9pOUjOVDpnpznT6Tq7H8HgGk6YEyUy50ur/mzkvsrN6fudIFUvkVR1mQ/p2cc95Dmd1t/qR0BZCBElykRsEBTqomzawAKC4PK58hNpIoUELQFMzItEawf3IrIJEW3CXkSUa7xEdC0MfO4lrfZodVdeUVR2bEK/CSeiSX6u0dZ+tnt6sZdrLQq0G7vJm4iRnl3dX1rl1fby8H4rp2vZTb2l0b6u97l+qAxso/8RWu5pgae9Wr8BMW4hpg677FLzcr2+wl7Ekn5EQOqbriWOjRll1j5NZLqXeiqrdmA35VGXVh79Vzptp96Qj/5i4el3+EwaaV2jTyuLhZI6EI3SKo/f3bONEfck+tlI2V3vxdbqp0+61qulN548N6HfqNOwLdm9oX3YktD2ub6u3Pog+zfkIW/9hG2kHYPd2YltXKMu+p1+RZy7lh3WdL5qc4Z2YBt1dQ/XmT/YZ1gvNvFSFnaSn3rpO+zo+jYvaW92kM41ymzMeVhXmZugl177yMtPZVEm5dMeFpDq4zN9zk+fqa+08tHX9Nv2z6XGBH1D2ZSTzZV92B4hhBDWLcsaqQ+zA4EpSuzbLU45pQovAp6wJ0LGFlzO4Ypc2zEQ+SMUnGUf23X5X8UCzy6Qc9QEn3+IRQgRRyGEEEIIS0VEfVgN0VPHPrxEAX0LjSiwiOE0jhE4AuIIgsikozSivqFGvD0E6Qy1o1L+dszDgieEEEIIYamJqA+r0b41gxh1BthZZed7HROaxvEIItU/9RGlF50fi+j/L+IM9xFH1HPRjo3sums9389OIYQQQghLTUR9GIW4d7beA4B+OkYyTTtfTtyH1fEQoqNJvlnEmWjnrJ0dDyGEEEJYDiLqQwghhBBCmHHyuF4IIYQQQggzTkR9CCGEEEIIM84aHr8JIYQQQgghrDQSqQ8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYaYp5f8A91ro9coVvFcAAAAASUVORK5CYII=" }
        }
      ]
    }
  ]
}

Error: The image_url.url must be the base64 data URL of the image

---

## Reply 21
**Author**: VIKASH PRASAD
**Posted**: 2025-01-24T02:02:04.952Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/24

Q8. how to handle the error ? @Jivraj

[http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094](http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094)

{“name”: “expense_balance”, “arguments”: “{“employee_id”: 52094}”}

TypeError: Failed to fetch

---

## Reply 22
**Author**: Varad Rajadhyax 
**Posted**: 2025-01-24T08:17:52.778Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/25

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for what appears to be an online quiz or assignment related to Large Language Models (LLMs). The UI includes:

*   A header with due date, score, and action buttons.
*   A section displaying recent saves.
*   A list of questions.
*   A dark mode toggle.

**2. Text Content:**

*   **Header:**
    *   "Due Sun, 2 Feb, 2025, 11:59 pm IST" - Indicates the deadline for the assignment.
    *   "Score: 2.75 / 8.5" - Shows the current score.
    *   "Check" - A button, presumably to check answers.
    *   "Save" - A button to save progress.
*   **Recent Saves:**
    *   "Recent saves" - A heading for the section.
    *   "Reload" - A button to reload a saved state.
    *   "from 24/1/2025, 12:25:51 pm. Score: 2.75" - Shows the date, time, and score of the saved state. This is repeated three times.
*   **Questions:**
    *   "Questions" - A heading for the section.
    *   A numbered list of questions, each with a title and the number of marks it's worth:
        1.  "LLM Sentiment Analysis (1 mark)"
        2.  "LLM Token Cost (0.75 marks)"
        3.  "Generate addresses with LLMs (1 mark)"
        4.  "LLM Vision (1 mark)"
        5.  "LLM Embeddings (0.75 marks)"
        6.  "Embedding Similarity (1 mark)"
        7.  "Vector Databases (1.5 marks)"
        8.  "Function Calling (1.5 marks)"
        9.  "Get an LLM to say Yes (1 mark)"

**3. Context and Purpose:**

The UI is designed for a user to complete an assignment or quiz related to LLMs. The user can:

*

Why is my score is out of 8.5? It should be 9.5 right?

It was 9.5 before a reload.

---

## Reply 23
**Author**: Sakthivel S
**Posted**: 2025-01-24T08:37:26.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/26

You should answer the third question every time the site reloads

---

## Reply 24
**Author**: Varad Rajadhyax 
**Posted**: 2025-01-24T10:06:51.736Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/27

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a coding environment, likely a web-based interface for writing and running Python code. It includes:

*   A code snippet defining a variable named `embeddings`.
*   A problem description outlining a coding task.
*   A text area for writing Python code.
*   A Python error traceback.

**2. Any text content visible:**

*   `embeddings = {"Packaging was excellent.": [-0.01674579456448555,-0.06481242924928665,-0.24050545692443848,0.042519159615039825,0.14857585728` (truncated). This appears to be a dictionary where the key is a phrase ("Packaging was excellent.") and the value is a list of floating-point numbers, likely representing an embedding vector.
*   "Your task is to write a Python function `most_similar(embeddings)` that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar." This is the problem statement.
*   "Write your Python code here:" This is a prompt for the user to enter their code.
*   "PythonError: Traceback (most recent call last): File "/lib/python312.zip/\_pyodide/\_base.py", line 523, in eval\_code.run(globals, locals) \^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\

For question no.6, there was some pre-written code there, right?

I am not able to see it now.

---

## Reply 25
**Author**: Varad Rajadhyax 
**Posted**: 2025-01-24T10:17:59.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/28

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a command-line interface (CLI) output, likely from a terminal or console window. It displays the execution of a Python script and the resulting error message.

**2. Any text content visible:**

The text content includes:

*   **Command Prompt:** `PS C:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS>` (This indicates the current directory in the PowerShell terminal)
*   **Python Execution Command:** `python -u "c:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS\request.py"` (This shows the command used to run the Python script named "request.py")
*   **Error Message (JSON format):**
    ```json
    {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
    ```
*   **Another Command Prompt:** `PS C:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS>`

**3. The context or purpose of what's displayed:**

The image shows that a Python script ("request.py") was executed, and it resulted in an error related to exceeding a quota. The error message is in JSON format, indicating that the script likely interacted with an API (Application Programming Interface). The specific API seems to be related to OpenAI, as the error message directs the user to OpenAI's documentation for API errors.

**4. Technical details (code screenshot or technical diagram):**

*   The error message is structured as a JSON object.
*   The error object contains the following keys:
    *   `message`: A human-readable description of the error.
    *   `type`: The type of error, which is "insufficient\_quota".
    *   `param`: A parameter related to the error (set to `None` in this case).
    *   `code`: A specific error code, also "insufficient\_quota".
*   The Python script "request.

I am getting insufficient_quota message for the 2nd question

---

## Reply 26
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-27T22:32:35.315Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/29

21f3002277:

The image_url.url must be the base64 data URL of the image

I tried downloading image for your dataset it is 2.36 KB in size.

Using base64 encoded string from `image_url.url` in your code when decoded comes out to be 8.18 KB, when I encoded image from your dataset and decoded it was 2.36 KB.

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Area (Base64*):** A large text area containing a long string of characters. This appears to be a Base64 encoded string. There are "copy", "clear", and "download" buttons next to it.
*   **Button ("Decode Base64 to Image"):** A button that likely triggers the decoding of the Base64 string into an image.
*   **Preview Image:** A section displaying a preview of the decoded image.
*   **Toggle Background Color:** A link to toggle the background color of the preview image.
*   **File Info:** A section providing details about the decoded image file.

**2. Text Content:**

*   **"Base64*"**: Label for the Base64 encoded data.
*   **"data:image/png;base64,..."**: The beginning of the Base64 encoded string, indicating that it represents a PNG image.
*   **"copy", "clear", "download"**: Buttons to copy, clear, and download the Base64 data.
*   **"Decode Base64 to Image"**: Text on the button to decode the Base64 string.
*   **"Preview Image | Toggle Background Color"**: Section header and link.
*   **"21f3002277@ds.study.iitm.ac.in 92893354"**: The content of the preview image, which is an email address and a number. The email address is highlighted in yellow.
*   **"File Info"**: Section header.
*   **"Resolution: 757x66"**: Image resolution.
*   **"MIME type: image/png"**: MIME type of the image.
*   **"Extension: png"**: File extension.
*   **"Size: 8.18 KB"**: File size.
*   **"Download: image.png"**: Link to download the image.
*   **"Bit depth: 8"**: Bit depth of the image.

**3. Context/Purpose:**

The image shows a UI for decoding a Base64 encoded string into an image. The user can input or paste a Base6

Hints : check if encoding is correct.

---

## Reply 27
**Author**: Abhay Sharma
**Posted**: 2025-01-28T04:11:34.779Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/30

Is it required to give SCT for the ROE of this course?

Thank you.

---

## Reply 28
**Author**: Carlton D'Silva
**Posted**: 2025-01-28T06:51:33.648Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/31

SCT is not required for ROE. ROE is not proctored.

Kind regards

---

## Reply 29
**Author**: K Hari Prasath
**Posted**: 2025-01-28T07:44:51.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/32

This is regarding Question 2 I tried to find number of tokens for the message. Using chatgpt identified the followings are valid English words for the given text in the question **D** **m** **Ay** **E r u y Vy** **V Ky** **P** **c**. then, checked with [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer). whatever number given by it seems to wrong.

@Jivraj could you inform me where I did mistake

---

## Reply 30
**Author**: Carlton D'Silva
**Posted**: 2025-01-28T07:59:50.162Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/33

@23f2003853 You have to find the input tokens from the json response you receive from the proxy.

---

## Reply 31
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-28T11:38:08.793Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/34

Hi VIKASH,

This problem must be because CORS not enabled or you are running your application inside wsl, if you using WSL then you would need to identify ipaddress of WSL and use it in place of `127.0.0.1`

kind regards

---

## Reply 32
**Author**: K Hari Prasath
**Posted**: 2025-01-28T11:48:12.076Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/35

Sir, from where can I  learn to locate the json response

---

## Reply 33
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-28T12:05:37.192Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/36

Hi @23f2003853 ,

You can learn from [Python’s Requests Library (Guide) – Real Python](https://realpython.com/python-requests/) tutorial about how to use requests module and see responses.

kind regards

---

## Reply 34
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-28T12:17:58.201Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/37

22f3000445:

I am getting insufficient_quota message for the 2nd question

Which url are you using to send request to openai.

---

## Reply 35
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-28T12:20:15.821Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/38

22f3000445:

For question no.6, there was some pre-written code there, right?

pre-written code is not required for question 6.

---

## Reply 36
**Author**: Divyasree
**Posted**: 2025-01-28T18:05:18.879Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/39

In the 6th question ,as I open the graded assignment all the time the new question is generated (NUMERICAL DATA) and the previous answer shows as incorrect answer

My doubt is that should I again and again answer the same quetion(6) all the time until the due passes?

Is there any alternative ways to look after this problem?

---

## Reply 37
**Author**: Saniya Naaz
**Posted**: 2025-01-29T04:19:54.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/40

**Image: Screenshot 2025-01-29 094832**
Here's a breakdown of the image content:

**1. UI Elements:**

*   The image appears to be a code editor or IDE, likely in a dark theme.
*   There's a toolbar at the top with icons for actions like "upload," "download," "copy," "link," "comment," "settings," "refresh," "delete," and "more options."

**2. Text Content:**

*   **JSON Request:**
    *   `"role": "user"`
    *   `"content": "List only the valid English words from these: B2k, D, Glr, ywpIvSQ, CR3XfA, dSVNJZip, "dwq, zP, G31jC0, VHXlo, 1Su, aAZw, pfqBkqU, wRUPIr, Go, n1Da, OMdJGxaVBk, OlrrH6x, "8zKs, UCX, 6XxK2bUYV4, A, jJxz, gv, P, xkyD, qn54iR2t"`
*   **Python Code:**
    *   `response = requests.post(url, headers=headers, json=data)`
    *   `# Check for successful response`
    *   `if response.status_code == 200:`
    *   `print(json.dumps(response.json(), indent=4))`
    *   `else:`
    *   `print(f"Request failed with status code: {response.status_code}")`
    *   `print(response.text) # Print the error response for debugging`
*   **Error Message:**
    *   `Request failed with status code: 429`
    *   `"error": {`
        *   `"message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors"`
        *   `"type": "insufficient_quota"`
        *   `"param": null`
        *   `"code": "insufficient_quota"`

**3

how to solve???

---

## Reply 38
**Author**: Saniya Naaz
**Posted**: 2025-01-29T04:49:26.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/41

getting quota full message for 7th question. How to get the answers then?

---

## Reply 39
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-29T15:28:56.065Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/42

Hi @Divya1 ,

Question 6 requires to write a generic code for finding most similar pair. If your code is doing so, pls mention exact steps that you have used to arrive at answer.

---

## Reply 40
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-29T15:30:02.829Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/43

[sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

Are you using this document?

---

## Reply 41
**Author**: K Hari Prasath
**Posted**: 2025-01-30T12:16:03.021Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/44

each time when I run the following code it gives me different number. None of the answer is correct. can help to fix the issue

**Image: image**
Here's a breakdown of the image content:

**1. What is shown in the image:**

*   The image shows a code snippet, likely Python, within a web browser window. It appears to be code for interacting with the OpenAI API, specifically the chat completions endpoint.

**2. Text Content:**

*   **URL:** `"https://api.openai.com/v1/chat/completions"` - This is the endpoint for the OpenAI chat completions API.
*   **Comments:** The code includes comments explaining the purpose of different sections. Examples:
    *   `# Use chat completions endpoint for GPT-4`
    *   `# List of input strings`
    *   `# Prepare the payload for Chat API (gpt-4 model)`
    *   `# Messages format`
    *   `# Send the POST request to OpenAI API`
    *   `# Parse the JSON response`
    *   `# Check if the request was successful`
*   **Headers:**
    *   `"Authorization": "Bearer (key)"` - This indicates that an API key is required for authentication.
    *   `"Content-Type": "application/json"` - Specifies that the data being sent is in JSON format.
*   **Data (Payload):**
    *   `"model": "gpt-4-mini"` - Specifies the model to use (likely a smaller version of GPT-4).
    *   `"messages": [{"role": "user", "content": user_message}]` - This defines the structure of the message sent to the API. It includes the role (user) and the content of the message.
*   **Code Logic:**
    *   `response = requests.post(url, headers=headers, json=data)` - Sends a POST request to the OpenAI API.
    *   `response_json = response.json()` - Parses the JSON response from the API.
    *   `if response.status_code == 200:` - Checks if the request was successful (status code 200 indicates success).
    *   `input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")` - Extracts the number of tokens used from the response.
    *   `

---

## Reply 42
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-30T21:04:36.088Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/46

Hi @23f2003853 ,

Please join tomorrow’s session, we can take it there, I am not sure why you facing this problem.

---

## Reply 43
**Author**: K Hari Prasath
**Posted**: 2025-01-31T00:15:29.928Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/47

Sure Sir. I am providing you the code below

import json
import os

api_key = key

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"  # Use chat completions endpoint for GPT-4
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# List of input strings
user_message = """
List only the valid English words from these: Q5YpaFZ0S, qZXgs13f, zyCiAjPh, JfcKU, G51N4, D, 9GbmmI27, jbdnhCd, 2dTr75, m, kS, lhO3Uc8e, SjpEmLl, u1cnuqk50, W54, 9, 7YWtUR, reoWxE2, Ay, ANRl2pFjL, E, 4hcE4cB, TZ2t, vck6a, Sb6vQ5K, CzQ, T5lYjxy1m, 2D, yG7PLW, mvgHmixMqn, YOPzsuhQ3, nSF7e6zFF, J60xA5WVp3, oz, vJM, vp2Zrsr, 59wiruyNzq, r, 8N, wv, z, MAKFrf5, 2L, 1IwLjzNpma, 5N20N7Zuq, 9dVp, tmUao0x, u, QRxy67, y, jrIvOZ, t3i, rptivNJF, Vy, 5WWaC1u, WC, xfoGYp, 350c94lf, Pc9oNu, 1bOnLseHUm, aguOp0jxE, Tbz, qX, 9amaVxKFh, bnBkkNN5jc, o7N4y6, V, Ky, ewWw0qcLnw, bbD7MBGM7x, c0l, P, TMFOMvW, c, THRovqGNKb, BV, XIZcX, J0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
    "model": "gpt-4o-mini",  
    "messages": [{"role": "user", "content": user_message}],  

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
    print(f"Input tokens used: {input_tokens}")
else:
    print(f"Request failed with status code {response.status_code}: {response_json}")```

---

## Reply 44
**Author**: Shalini Saravanan
**Posted**: 2025-01-31T09:20:32.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/48

Hello Sir,

I am unable to recieve a proper output for q1 of ga3.

This is my test message. Its been given in two lines.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a snippet of text displayed on a dark background, likely from a code editor, terminal, or similar application. It shows two lines of alphanumeric characters.

**2. Any text content visible:**

The text content is as follows:

*   **Line 1:** `2 b7 rkS94mn4`
*   **Line 2:** `AM dNG4j EVEvK24Ev VEpiI G LeeHS`

**3. The context or purpose of what's displayed:**

Without further context, it's difficult to determine the exact purpose. However, the alphanumeric strings suggest the following possibilities:

*   **Identifiers/Hashes:** The strings could be unique identifiers, hash values, or keys used in a software system.
*   **Data:** The strings could represent data values or codes within a dataset.
*   **Log Output:** The text could be part of a log file, where each line represents an event or message.
*   **Configuration:** The strings could be part of a configuration file, where each line represents a setting or parameter.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The text is displayed in a monospaced font, which is common in code editors and terminals.
*   The number "2" on the first line is colored in light blue.
*   The letter "G" on the second line is colored in green.
*   The background is dark, which is a common theme for code editors to reduce eye strain.

In summary, the image shows a snippet of alphanumeric text, likely from a technical context such as software development, data analysis, or system administration. The exact meaning of the text is unclear without additional information.

The below is my code for the question.

import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's  GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4  AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": system_message},  # System message
        {"role": "user", "content": user_message}       # One user message
    ],
    "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
    print("AI Response:", choice["message"]["content"])

I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative

`user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"`

The error message i keep receiving is as below.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of code, likely from a programming environment or console. It appears to be a JavaScript object assignment, specifically a `payload` object.  Below the code, there's an error message displayed. The code and error are presented against a dark background, typical of code editors or terminals in dark mode.

**2. Any text content visible:**

*   `payload = {`
*   `Error: The user message must be 2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS, not 2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS`

**3. The context or purpose of what's displayed:**

The context is likely a software development scenario where a user is trying to send a message (possibly through an API or some other system). The error message indicates that the message being sent doesn't meet certain criteria. Specifically, the error suggests that the message should be different from the string "2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS". It's possible there's a validation rule in place that prevents sending the same message twice, or that the message is being interpreted as a default or placeholder value.

**4. Technical details (if it's a code screenshot or technical diagram):**

*   The code snippet `payload = {` suggests that the `payload` variable is being assigned an object. The contents of the object are not fully visible, but the error message implies that it contains a "user message" field.
*   The error message itself is a string, likely generated by the system's validation logic. The "must be... not..." structure of the error message indicates a comparison is being made between the user's input and a forbidden value.
*   The error message is highlighted with a red border, indicating that it is an error.

Kindly advice on how to proceed.

Thanks and Regards

Shalini

---

## Reply 45
**Author**: Carlton D'Silva
**Posted**: 2025-01-31T09:37:36.551Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/49

Hi Shalini,

Your `user_message` is incorrect. I looked at your exact GA and it works if you make sure your `user_message` is precisely what is given to you.

Hint: How do you store a multi-line variable in python?

Kind regards

---

## Reply 46
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-01-31T10:42:36.589Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/50

Hello, could anyone please confirm that GA 3 is worth 9.5 points? Since our GAs are typically 10 marks apiece, I wanted to inquire about and obtain clarification on this.

Thank you in advance.

---

## Reply 47
**Author**: Yogesh
**Posted**: 2025-01-31T14:24:33.385Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/51

I was unable to make the answer box in Question 3 visible. I was only able to make white space appear there, but couldn’t make it so that answer can be input to the box.

---

## Reply 48
**Author**: Carlton D'Silva
**Posted**: 2025-01-31T14:40:38.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/52

In addition to CSS classes there is also a tag attribute acting on it. Check carefully.

Kind regards

---

## Reply 49
**Author**: Maheshwar Ture
**Posted**: 2025-01-31T16:31:15.592Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/53

I am getting below error for Q6 if i am importing sklearn libarary

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a Python error message, specifically a traceback, within a UI element that appears to be a console or output window. The error is related to a missing module.

**2. Any text content visible:**

The text content is as follows:

*   `PythonError: Traceback (most recent call last): File "/lib/python312.zip/_pyodide/_base.py", line 523, in eval_code.run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File "/lib/python312.zip/_pyodide/_base.py", line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "", line 4, in `
*   `ModuleNotFoundError: No module named 'scipy' The module 'scipy' is included in the Pyodide distribution, but it is not installed. You can install it by calling: await micropip.install("scipy") in Python, or await pyodide.loadPackage("scipy") in JavaScript See https://pyodide.org/en/stable/usage/loading-packages.html for more details.`

**3. The context or purpose of what's displayed:**

The error message indicates that a Python script attempted to import the `scipy` module, but the module was not found. The message also suggests that the environment is likely Pyodide, a Python distribution for the browser. It provides instructions on how to install the `scipy` module within the Pyodide environment, either using `micropip.install("scipy")` in Python or `pyodide.loadPackage("scipy")` in JavaScript. It also provides a link to the Pyodide documentation for more information on loading packages.

**4. Technical details if it's a code screenshot or technical diagram:**

*   **Error Type:** `ModuleNotFoundError`
*   **Missing Module:** `scipy`
*   **Environment:** Likely Pyodide (based on the file paths and the installation instructions)
*   **Python Version:** Python 3.12 (based on the file path `/lib/python31

---

## Reply 50
**Author**: RAJ K BOOPATHI
**Posted**: 2025-02-01T03:45:32.917Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/54

Hi team, I am using OpenAI API key for solving Q7 and getting the error like below

{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

Is it necessary to pay for the OpenAI API key? Is there any other way?

---

## Reply 51
**Author**: Carlton D'Silva
**Posted**: 2025-02-01T05:38:06.960Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/57

@21f2000588

Sure does add up to 9.5 , unless you want another question  :wink: 

Kind regards

---

## Reply 52
**Author**: Anand S
**Posted**: 2025-02-01T05:53:30.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/58

Yeah, after all these years of learning and teaching computing, I realize I can’t even count to 10 correctly anymore.

**Image: Screenshot**
Here's a detailed description of the image:

**Overall:**

The image is a four-panel comic strip featuring the character Calvin from the comic strip "Calvin and Hobbes." The comic is drawn in black and white.

**Panel 1:**

*   **Visuals:** Calvin is sitting at his school desk with his hand raised. He's wearing his striped shirt.
*   **Text:** "MISS WORMWOOD, MY DAD SAYS WHEN HE WAS IN SCHOOL, THEY TAUGHT HIM TO DO MATH ON A SLIDE RULE."

**Panel 2:**

*   **Visuals:** Calvin is standing, looking slightly exasperated.
*   **Text:** "HE SAYS HE HASN'T USED A SLIDE RULE SINCE, BECAUSE HE GOT A FIVE-BUCK CALCULATOR THAT CAN DO MORE FUNCTIONS THAN HE COULD FIGURE OUT IF HIS LIFE DEPENDED ON IT."

**Panel 3:**

*   **Visuals:** Calvin is back at his desk, smiling.
*   **Text:** "GIVEN THE PACE OF TECHNOLOGY, I PROPOSE WE LEAVE MATH TO THE MACHINES AND GO PLAY OUTSIDE."

**Panel 4:**

*   **Visuals:** Calvin is slumped over his desk, looking dejected.
*   **Text:** "MY BILLS ALWAYS DIE IN SUBCOMMITTEE."

**Context/Purpose:**

The comic strip is a humorous commentary on the changing landscape of mathematics education and technology. Calvin's father learned to use a slide rule, but now calculators are more powerful and accessible. Calvin suggests embracing technology and playing outside instead of doing math. The final panel is a joke about the difficulty of getting anything done in a bureaucracy, comparing it to his "bills" (likely referring to schoolwork) dying in a "subcommittee."

**Technical Details:**

*   The comic is dated "4-25" (likely April 25th).
*   There's a copyright notice: "© 1992 Watterson. Distributed by Universal Press Syndicate."

---

## Reply 53
**Author**: RAJ K BOOPATHI
**Posted**: 2025-02-01T05:55:44.883Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/59

@Jivraj Please let me know if the code is needed for this. I can share the code generated by chatgpt

---

## Reply 54
**Author**: Wasim Ansari
**Posted**: 2025-02-01T13:52:03.153Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/60

@Jivraj , @carlton  Dear Sirs, I need help in solving this question. I have the same issue. I have tried tokenizer tool, tried writing request code but still couldn’t get the correct answer. I have tried numerous time and ended up consuming lot of tokens . What should be the optimal approach in this question?

  "id": "chatcmpl-Aw7eXQ8hciiQ0ZedatQEifFGxnLhQ",
  "object": "chat.completion",
  "created": 1738415805,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The valid English words from the given list are:\n\n- a\n- I\n- o\n- t\n- U\n- w\n- y\n- z",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 532,
    "completion_tokens": 34,
    "total_tokens": 566,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.01662212,
  "cost": 0.001863,
  "monthlyRequests": 41,
  "costError": "crypto.createHash is not a function"
}

---

## Reply 55
**Author**: Raunak Pugalia
**Posted**: 2025-02-02T08:10:42.643Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/62

Tried hundreds of different prompts, different situations but in Q9 AI is not responding “Yes”. Is there anything i am missing?

---

## Reply 56
**Author**: K Hari Prasath
**Posted**: 2025-02-02T12:41:10.201Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/64

Dear Sir, I got the answer in json but none out put is correct. Please help me to correct the code

curl [https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions) \                                             >   -H “Content-Type: application/json” \                                                                               >   -H “Authorization: Bearer $TOKEN” \                                                                                 '{                                                                                                                          >   -d ‘{                                                                                                           >     “model”: “gpt-4o-mini”,                                                                                            "messa>     “messages”: [{                                                                                             >       “role”: “user”,                                                                                                      "c>       “content”: “List only the valid English words from these: zqndWw3FB, kM, K, njuHs9A, r, lkXJ1lG, Z, yLHDClp, G1Db, 7, m, MYieYF3B, pFTQ1JU8Fj, RL9n6kE, EVpChB, V6iCpP, 9YwiwAnBc5, R, UM, mrnyc, 4ej9x, 8X, CQA9, jHC, uL4G6, f, zzaozWC9, 0qsOenEndF, qaZ2WoX, nXGZ”                                                                                   >     }]                                                                                                                >   }’                                                                                                                  {                                                                                                                         “id”: “chatcmpl-AwTPGH241yjyg9EkO1t1tbeGU7KCu”,                                                                         “object”: “chat.completion”,                                                                                            “created”: 1738499426,                                                                                                  “model”: “gpt-4o-mini-2024-07-18”,                                                                                      “choices”: [                                                                                                              {                                                                                                                         “index”: 0,                                                                                                             “message”: {                                                                                                              “role”: “assistant”,                                                                                                    “content”: “The valid English words from your list are:\n\n- my\n- is\n- an\n- or\n- in\n\n(Note: This assumes a focus on short English words. Longer words or specific proper nouns may also exist but were not included in this selection.)”,                                                                                                                         “refusal”: null                                                                                                       },                                                                                                                      “logprobs”: null,                                                                                                       “finish_reason”: “stop”                                                                                               }                                                                                                                     ],                                                                                                                      “usage”: {                                                                                                                “prompt_tokens”: 160,                                                                                                   “completion_tokens”: 53,                                                                                                “total_tokens”: 213,                                                                                                    “prompt_tokens_details”: {                                                                                                “cached_tokens”: 0,                                                                                                     “audio_tokens”: 0                                                                                                     },                                                                                                                      “completion_tokens_details”: {                                                                                            “reasoning_tokens”: 0,                                                                                                  “audio_tokens”: 0,                                                                                                      “accepted_prediction_tokens”: 0,                                                                                        “rejected_prediction_tokens”: 0                                                                                       }                                                                                                                     },                                                                                                                      “service_tier”: “default”,                                                                                              “system_fingerprint”: “fp_72ed7ab54c”                                                                                 }

---

## Reply 57
**Author**: Vaishali
**Posted**: 2025-02-02T15:38:32.738Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/65

Pls give some kind of clue. It seems like a waste of so much time!

---

## Reply 58
**Author**: Raunak Pugalia
**Posted**: 2025-02-02T15:44:35.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/67

i agree, i have wasted around 300 requests (prompts) and got nothing.

---

## Reply 59
**Author**: VIKASH PRASAD
**Posted**: 2025-02-03T06:54:57.348Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/69

Sir I am stuck in Q4. how to handle the error please help me @Jivraj @carlton

Error: The image_url.url must be the base64 data URL of the image

---

## Reply 60
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-03T07:22:48.722Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/70

Okay thank you sir, for the clarification.

---

## Reply 61
**Author**: Yogesh
**Posted**: 2025-02-03T14:11:25.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/71

You have to download that image, and find the base_url of that image.

---

## Reply 62
**Author**: VIKASH PRASAD
**Posted**: 2025-02-03T14:22:52.043Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/72

from where to download

---

## Reply 63
**Author**: Yogesh
**Posted**: 2025-02-03T15:09:11.873Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/73

The image is part of the question.

---

## Reply 64
**Author**: Anand S
**Posted**: 2025-02-03T15:28:45.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/74

For those who want to experiment with GPT-4o Mini (or other models), [Github Models](https://github.com/marketplace/models) is free. You can explore and compare models, including GPT-4o Mini, DeepSeek R1, and others.

It has rate limits, so you can’t use it in production, but is a good place to prototype applications and experiment with prompts.

Please let me know if you face any problems accessing it.

---

## Reply 65
**Author**: Dwarakesh
**Posted**: 2025-02-03T18:25:21.354Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/75

how to answer the question in first place ?

---

## Reply 66
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-03T22:07:57.870Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/76

Check if you are requesting through anand sir’s proxy [AI Proxy](https://aiproxy.sanand.workers.dev/).

---

## Reply 67
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-03T22:10:01.674Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/77

sklearn might be using scipy for some purpose, just install it, it should work.

Btw what are you trying to do with Sklearn?

---

## Reply 68
**Author**: Maheshwar Ture
**Posted**: 2025-02-04T03:13:45.199Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/78

thanks for the reply i was using cosine function but got another solution.

---

## Reply 69
**Author**: Naga durga prasad E
**Posted**: 2025-02-04T09:51:48.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/80

Q2 LLM Token Cost ,

We have [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) , which helps us count tokens in a string, shouldn’t this be a better way than calling the API? However the returned value does not show as correct answer!

---

## Reply 70
**Author**: Tanmay Garg
**Posted**: 2025-02-04T13:27:09.694Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/81

Hi guys, just wanted to share that I found it hysterical when I saw this question:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a web page, likely an online assignment or coding challenge. It displays a problem description, instructions, and hints related to generating a JSON body for an OpenAI chat completion API call. The page includes UI elements like a header with tabs, a score indicator, "Check all" and "Save" buttons, and a "Check" button at the bottom.

**2. Text Content:**

*   **Header:** "My Dashboard - IIT Madras Onl", "Graded Assignment 3 :: IITM On", "Ex TDS 2025 Jan GA3 - Large Lang", "API Reference - OpenAI API", "TDS - LLM Extraction - YouTube"
*   **Assignment Details:** "Due Wed, 5 Feb, 2025, 11:59 pm IST", "Score: 1/9.5", "Check all", "Save"
*   **Constraints:**
    *   "type": "string": ... which is a string.
    *   "required": ["steps", "final_answer"]: You must add "required": [...] and include all fields in the object.
    *   "additionalProperties": false: OpenAI requires every object to have "additionalProperties": false.
*   **Problem Description:** A paragraph describing RapidRoute Solutions, a logistics company that needs to generate realistic U.S. addresses using an OpenAI GPT-4o-Mini model. The addresses must be structured JSON data.
*   **Instructions:**
    *   The engineering team at RapidRoute is tasked with designing a service that uses OpenAl's GPT-40-Mini model to generate fake but plausible address data.
    *   As part of the integration process, you need to write the body of the request to an OpenAI chat completion call that:
        *   Uses model gpt-40-mini
        *   Has a system message: Respond in JSON
        *   Has a user message: Generate 10 random addresses in the US
        *   Uses structured outputs to respond with an object addresses which is an array of objects with required fields: apartment (string) zip (number) latitude (number).
        *   Sets additionalProperties to false to prevent additional properties.
    *   Note that

Like I literally showed this question to my mother and younger bro, stating the fact we ourselves had enable the answer box, they laughed there pants off… :joy:  :joy: 

More courses could be like this.

---

## Reply 71
**Author**: Andrew David
**Posted**: 2025-02-04T13:59:46.793Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/82

**Q4**

s3 string was given by

image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"

s4 string given by : 

used this [link ](https://www.base64-image.de/)  to generate image url

 Then checked them both, they were the same

for x,y in zip(s3,s4):
  if (x != y):
    print(x,y)

i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?

I know i’m missing something, but why?

---

## Reply 72
**Author**: Andrew David
**Posted**: 2025-02-04T14:05:18.252Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/83

**Image: Screenshot 2025-02-04 193342**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a coding environment, likely an online platform for learning or practicing Python. It presents a coding problem, a code editor area, and an error message.

**2. Text Content:**

*   **Problem Description:**
    *   "Your task is to write a Python function `most_similar(embeddings)` that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar."
    *   "Write your Python code here:"
*   **Code Editor:**
    *   `import numpy`
    *   `def most_similar(embeddings):`
    *   `# Your code here`
    *   `return (phrase1, phrase2)`
*   **Feedback:**
    *   "Incorrect answer"
*   **Error Message:**
    *   `PythonError: Traceback (most recent call last): File "/lib/python312.zip/_pyodide/_base.py", line 523, in eval_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File "/lib/python312.zip/_pyodide/_base.py", line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "", line 11, in  File "", line 8, in most_similar NameError: name 'phrase1' is not defined`

**3. Context and Purpose:**

The image depicts a user attempting to solve a coding problem related to finding the most similar pairs of embeddings using cosine similarity. The user has written some initial code, but it contains an error, as indicated by the "Incorrect answer" feedback and the Python traceback. The purpose is likely to provide a coding exercise and feedback to help the user learn and improve their Python skills, specifically in the area of natural language processing or machine learning.

**4. Technical Details (Code and Error):**

*   **Code:** The code imports the `numpy` library, defines a function `most_similar` that takes `embeddings` as input, and attempts to return a tuple `

---

## Reply 73
**Author**: PalakAnand
**Posted**: 2025-02-04T14:05:45.580Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/84

**Image: Screenshot 2025-02-04 at 19.32.21**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** A text input field with a red border. It contains the URL "http://127.0.0.1:8000/execute". There's a red exclamation mark icon inside the input field on the right side, indicating an error or warning.
*   **Text Labels/Instructions:** Several lines of text provide context and instructions.
*   **Button:** A blue "Check" button is at the bottom left.

**2. Text Content:**

*   "Make sure you enable CORS to allow GET requests from any origin." (This is likely above the visible portion of the image)
*   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
*   "http://127.0.0.1:8000/execute" (This is the content of the input field)
*   "SyntaxError: "undefined" is not valid JSON" (Error message displayed below the input field)
*   "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."
*   "Check" (Text on the button)

**3. Context and Purpose:**

The image shows a UI for testing or validating an API endpoint. The user is prompted to enter the URL of their API endpoint. The system then attempts to send a GET request to that URL with a query parameter "q" containing a task. The system will verify if the response matches the expected response. The error message "SyntaxError: "undefined" is not valid JSON" suggests that the API is returning an invalid JSON response, or no response at all.

**4. Technical Details:**

*   The URL "http://127.0.0.1:8000/execute" indicates a local development server running on port 8000.
*   The system is using a GET request with a query parameter "q" to send a task to the API.
*   The system expects a valid JSON response from the API.
*   CORS

This is in context to Q8. This is a screenshot of the response I am getting when i run the same API on my FastAPI/docs response page, it gives the correct response. But when I check it on the assignment page i get the following error. If you would like to know the code, pls let me know. @carlton @Jivraj

---

## Reply 74
**Author**: Sudhish Narayan S
**Posted**: 2025-02-04T16:16:35.495Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/85

Good Evening, I have a doubt regarding 7th and 8th question. I am getting this error of expecting three matches while saving. But, Externally when I check this API, I tried considerable test cases, and I am getting the output correctly. Can you please check this and give a solution. Thank You

**Image: Screenshot 2025-02-04 214334**
Here's a detailed description of the image:

1.  **What is shown in the image:** The image displays a snippet of code, specifically a Python dictionary. The dictionary contains one key-value pair.

2.  **Text content visible:**
    *   `{'matches': ['banana', 'watermelon', 'jamaica']}`

3.  **Context/Purpose:** The code represents a dictionary where the key is 'matches' and the value is a list of strings: 'banana', 'watermelon', and 'jamaica'. This could be used in a program to store or represent a list of items that match a certain criteria.

4.  **Technical Details:**
    *   The code is written in Python syntax.
    *   The data structure is a dictionary, which is a collection of key-value pairs.
    *   The key 'matches' is a string.
    *   The value associated with 'matches' is a list of strings.
    *   The strings in the list are 'banana', 'watermelon', and 'jamaica'.
    *   The strings are enclosed in single quotes, which is a common way to represent strings in Python.

**Image: Screenshot 2025-02-04 214319**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or development tool. It includes text instructions, a text input field, and an error message.

**2. Any text content visible:**

*   "Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers."
*   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity"
*   "http://127.0.0.1:8000/similarity" (This appears in the input field)
*   "Error: Expected 3 matches"

**3. The context or purpose of what's displayed:**

The UI is guiding the user to input the correct API URL endpoint for their implementation. The context seems to be related to configuring Cross-Origin Resource Sharing (CORS) to allow specific HTTP methods (OPTIONS and POST). The error message suggests that the entered URL is not matching the expected format or criteria.

**4. Technical details:**

*   The URL "http://127.0.0.1:8000/similarity" is a local address, indicating that the API is likely running on the user's machine (localhost) on port 8000. The "/similarity" part suggests that the API is related to some kind of similarity calculation or comparison.
*   The error message "Error: Expected 3 matches" implies that the system is expecting the URL to match a certain pattern or criteria, possibly involving a regular expression or a specific number of segments in the URL path.
*   The presence of CORS instructions indicates that the application is likely making requests to this API from a different origin (domain, protocol, or port). CORS is a browser security mechanism that restricts cross-origin HTTP requests.

---

## Reply 75
**Author**: Sudhish Narayan S
**Posted**: 2025-02-04T17:52:10.076Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/86

This is regarding the 8th question. Same here, I am getting the answer for all the test cases, but then also, I am getting error in the portal while saving. Please help me out here. Thank You.

**Image: Screenshot 2025-02-04 232048**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Browser Window:** The image shows a portion of a web browser window. The address bar is visible at the top.
*   **Address Bar:** The address bar contains a URL.
*   **"Pretty-print" Checkbox:** There's a checkbox labeled "Pretty-print".
*   **JSON Output:** Below the checkbox, there's a block of text formatted as JSON.

**2. Text Content:**

*   **URL:** The URL in the address bar is `127.0.0.1:8001/execute/?q="Calculate%20performance%20bonus%20for%20employee%2010056%20for%202025."`
*   **"Pretty-print"**
*   **JSON:** The JSON content is:
    ```json
    {"name":"calculate_performance_bonus", "arguments":"{\"employee_id\": 10056, \"current_year\": 2025}"}
    ```

**3. Context and Purpose:**

*   **API Endpoint:** The URL suggests that the browser is accessing an API endpoint at `127.0.0.1:8001/execute`.
*   **Query Parameter:** The `?q=` part of the URL indicates a query parameter named "q". The value of this parameter is a string that describes a request to "Calculate performance bonus for employee 10056 for 2025". The spaces are encoded as `%20`.
*   **JSON Response:** The JSON output is likely the response from the API endpoint. It indicates that the API call is for a function named "calculate\_performance\_bonus". The "arguments" field contains a JSON string with the employee ID (10056) and the current year (2025).
*   **"Pretty-print" Checkbox:** The "Pretty-print" checkbox suggests that the JSON output can be formatted for better readability if the checkbox is selected.

**4. Technical Details:**

*   **JSON Structure:** The JSON response has a simple structure with two key-value pairs: "name" and "arguments".
*   **Nested

**Image: Screenshot 2025-02-04 231847**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or development tool. It consists of:

*   A text prompt or question.
*   An input field (text box) with a URL entered.
*   An error message displayed below the input field.

**2. Any text content visible:**

*   **Question:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
*   **Input Field Content:** "http://127.0.0.1:8001/execute"
*   **Error Message:** "TypeError: Failed to fetch"

**3. The context or purpose of what's displayed:**

The UI is designed to collect an API URL from the user. The question prompts the user to enter the URL for their API implementation. The example URL provided (http://127.0.0.1:8000/execute) suggests a local development environment. The error message "TypeError: Failed to fetch" indicates that the application attempted to access the URL provided in the input field, but the request failed. This could be due to several reasons, such as:

*   The server at the specified URL is not running.
*   There is a network connectivity issue.
*   The URL is incorrect.
*   The server is not configured to allow cross-origin requests (CORS).

**4. Technical details (based on the code screenshot):**

*   The error "TypeError: Failed to fetch" is a common JavaScript error that occurs when the `fetch()` API (used for making network requests) encounters a problem.
*   The URLs (http://127.0.0.1:8000/execute and http://127.0.0.1:8001/execute) use the IP address 127.0.0.1, which is the loopback address (localhost). This means the application is trying to connect to a server running on the same machine.
*   The URLs also specify different ports (8000 and 8001), indicating that the application might be expecting the

---

## Reply 76
**Author**: Jayaram
**Posted**: 2025-02-04T18:07:26.462Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/87

For question 1 getting the below response … not sure what it means

ythonError: Traceback (most recent call last): File “/lib/python312.zip/_pyodide/_base.py”, line 523, in eval_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File “/lib/python312.zip/_pyodide/_base.py”, line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File “”, line 53, in  TypeError: unhashable type: ‘dict’

---

## Reply 77
**Author**: Jayaram
**Posted**: 2025-02-05T01:44:08.545Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/88

@carlton

for question 2 what does  the below instruction mean … also how to indicate this in a prompt ’ Remember: indicating that this is a `user` message takes up a few extra tokens. You actually need to make the request to get the answer."

---

## Reply 78
**Author**: Jayaram
**Posted**: 2025-02-05T03:57:27.717Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/89

For token count query , trying to do something like below any issues with this

import requests
import json
from google.colab import userdata
def generate_readme_content(proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""       
    SNyFiNTb, BUkDfo0tR, x3x, 6NE8Rq833, Re7, Vth9bYJ0pK, pnI, JAXpFb, BRPE, o, 5xVQe, iY8yVT, 69w, LjLCzs, MJ1g, wBR, 0H, 6bK, AMw, Vrxiux, dqZysH, yD82hcr, FZrwV8Zjq, Xb2, quLpdQqxd1, lqSLbI, HerfhK2, rNPU, 9K1C, 0ywhX2s4O9, mjZ, sR9gCC, 2WVSfwWEae, c, DtWnfOncFj, qjK8P7xh, 0xraHn7RMa, OCmQIi3tbU, S2K, F, q5mO, yZt, X, zd, se0ss3k, uU, yCRCi, S3bMfb, qZ4dh, M7, uhxgDvG3, 696g, 9k, l5U, bH, LVXw1fdWFi, 0kU68gGP, WuyD, V, kVKQ1Y8, kLjMDoEmIN, EYHs7qsabQ, sWrC8vN7n, oAJZP, YLd, mi6Jmxgf, cb9UDdap, kzuot, R0eA2V, mr7SctL49, Td5, in, hxvi, MDg, AAK, uLBF889bO5, Z7z, AO0c, nbc, bE6Rsdw5b, 0, pBjOAuPN8A, 9C3, K, 8, yZyCBPz   
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant to count the number of english words in a message. Find the number of input tokens used for  a message lile below. Try excluding tokens used for understanding this prompt"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
        # Send a POST request to the proxy server
    response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",
                     
            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
    response_data = response.json()
    return response_data
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
tokenjson=generate_readme_content(proxy_url,auth_token)
print(tokenjson)

---

## Reply 79
**Author**: Naman Gupta
**Posted**: 2025-02-05T07:08:49.236Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/90

I GOT THE CORRECT ANSWER F0R QUES 7 & 8 STILL MY SCORE IS SHOWING 8 DOES ANYONE KNOW HOW TO DO THIS ?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, specifically instructions for an online assessment or quiz. The UI includes a title, a list of instructions, a note, and a call to action with a link. There are also two icons on the right side of the image.

**2. Any text content visible:**

*   **Title:** "TDS 2025 Jan GA3 - Large Language Models"
*   **Section Header:** "Instructions"
*   **Instructions (numbered list):**
    1.  "Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure.)"
    2.  "Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times."
    3.  "Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated."
    4.  "Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters."
    5.  "Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser."
    6.  "Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want."
    7.  "It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed."
*   **Note:** "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."
*   **Call to Action:** "Have questions? Join the discussion on Discourse"

**3. The context or purpose of what's displayed:**

The image presents instructions for a quiz or exam focused on "Large Language Models." The instructions provide guidance on how to approach the assessment, including checking answers, saving progress, and using external resources. The instructions also mention that the quiz is "hackable," suggesting that students are allowed to examine the underlying code.

**4. Technical details if it's a code screenshot or technical diagram:**

The image is not a code screenshot

---

## Reply 80
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-05T10:25:25.132Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/91

Use addition : to add up your score for each question.

eq:

1+ 1 = 2

Fractions are harder

1.5 + 1 = 2.5

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a list of questions, likely for an exam, assignment, or quiz. Each question is numbered and followed by a topic related to Large Language Models (LLMs). Each question also has a mark value associated with it.

**2. Any text content visible:**

The text content includes:

*   **Title:** "Questions"
*   **Question List:**
    1.  LLM Sentiment Analysis (1 mark)
    2.  LLM Token Cost (0.75 marks)
    3.  Generate addresses with LLMs (1 mark)
    4.  LLM Vision (1 mark)
    5.  LLM Embeddings (0.75 marks)
    6.  Embedding Similarity (1 mark)
    7.  Vector Databases (1.5 marks)
    8.  Function Calling (1.5 marks)
    9.  Get an LLM to say Yes (1 mark)

**3. The context or purpose of what's displayed:**

The image presents a set of questions related to LLMs, likely for educational or assessment purposes. The topics cover various aspects of LLM usage, including sentiment analysis, cost analysis, generation, vision, embeddings, similarity, databases, function calling, and prompting. The mark values indicate the relative weight or difficulty of each question.

**4. Technical details if it's a code screenshot or technical diagram:**

This image is not a code screenshot or technical diagram. It's a simple list of questions. However, the topics themselves are technical and relate to the field of Natural Language Processing and Machine Learning, specifically concerning Large Language Models.

---

## Reply 81
**Author**: Tanmay Garg
**Posted**: 2025-02-05T10:27:53.411Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/92

To this question I have checked values ranging from 6 to 13 none of them are correct, using openAI Tokenizer online tool.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a web page, likely an online assessment or assignment. It shows a question related to LLM (Large Language Model) token cost. The UI elements include:

*   A browser address bar showing the URL: `exam.sanand.workers.dev/tds-2025-01-ga3`
*   A timer indicating "08:04:14 left".
*   A score display showing "Score: 0 / 9.5".
*   Buttons labeled "Check all" and "Save".
*   A question section titled "LLM Token Cost (0.75 marks)".
*   A text area for the user to input the "Number of tokens".
*   A "Check" button at the bottom.
*   A Windows taskbar at the very bottom with various application icons.

**2. Any text content visible:**

*   **Question Title:** "LLM Token Cost (0.75 marks)"
*   **Context:** A description of LexiSolve Inc. as a startup using OpenAI's language models for various AI tasks. It emphasizes the importance of token accounting for cost management.
*   **Task Description:** The task involves understanding text tokenization. The user needs to determine the number of tokens used when making a request to OpenAI's GPT-4o-Mini with a specific user message.
*   **Specific Instruction:** "List only the valid English words from these:" (followed by a blacked-out section, presumably containing a list of words).
*   **Question:** "... how many input tokens does it use up?"
*   **Input Field Label:** "Number of tokens:"
*   **Hint:** "Remember: indicating that this is a user message takes up a few extra tokens. You actually need to make the request to get the answer."
*   **Button Label:** "Check"
*   **Windows Activation Notice:** "Activate Windows. Go to Settings to activate Windows."

**3. The context or purpose of what's displayed:**

The image shows a question from an online assessment focused on understanding how language models tokenize text. The user is presented with a scenario where they need to determine the number of tokens a specific prompt would use

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface for a tokenizer tool, likely from OpenAI. The interface allows users to input text and see how it's broken down into tokens. The UI elements include:

*   A text input area where the user can type or paste text.
*   "Clear" and "Show example" buttons.
*   Displays for the number of tokens and characters in the input text.
*   Tabs labeled "Text" and "Token IDs" (the "Text" tab is currently selected).
*   Navigation elements at the top, including "Playground," "Dashboard," "Docs," and "API reference."
*   Browser tabs at the top of the screen.

**2. Any text content visible:**

*   **Browser Tab:** "Tokenizer" and the URL "platform.openai.com/tokenizer"
*   **Top Navigation:** "Playground," "Dashboard," "Docs," "API reference"
*   **Project:** "personale / Default project"
*   **Buttons:** "Clear," "Show example"
*   **Metrics:** "Tokens 10," "Characters 47"
*   **Input Text:** "List only the valid English words from these:" (with different words highlighted in different colors)
*   **Tabs:** "Text," "Token IDs"
*   **Explanatory Text:**
    *   "A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This translates to roughly 3/4 of a word (so 100 tokens ~= 75 words)."
    *   "If you need a programmatic interface for tokenizing text, check out our `tiktoken` package for Python. For JavaScript, the community-supported `@dbdq/tiktoken` package works with most GPT models."
*   **Windows Activation:** "Activate Windows. Go to Settings to activate Windows."

**3. The context or purpose of what's displayed:**

The image shows a tool for understanding how text is tokenized, which is a crucial step in many natural language processing (NLP) tasks. Tokenization is the process of breaking down text into smaller units (tokens) that can be processed by machine learning models. The tool likely helps developers and researchers understand

Please help me were I am going wrong.

---

## Reply 82
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-05T10:29:00.515Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/93

22f3002723:

`user` message

that means it should be a user message

messages = [
{
"role":"user",
"content":"message"
}
]

---

## Reply 83
**Author**: Tanmay Garg
**Posted**: 2025-02-05T10:51:47.566Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/94

Keep getting this error.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser interface, likely a coding assessment or online learning platform. It displays a question related to API endpoints and function calling with OpenAI. There are UI elements like a timer, score, "Check all" and "Save" buttons, and a text input field. There's also a code snippet displayed as an example.

**2. Text Content:**

*   **Title Bar:** "My Dash...", "Graded...", "GA3 - La...", "Ex TDS 202...", "Async DI...", "uv: Pythe...", "Running...", "127.0.0.1...", "4.75+1.5...", "Tokenize...", "You can...", "+"
*   **URL:** exam.sanand.workers.dev/tds-2025-01-ga3
*   **Timer:** 07:38:35 left
*   **Score:** 0/9.5
*   **Buttons:** Check all, Save, Check
*   **Example Response:**
    ```json
    {
    "matches": [ "Contents of document 3", "Contents of document 1", "Contents of document 2" ]
    }
    ```
*   **Question Text:**
    *   "Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2"."
    *   "Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers."
    *   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity"
    *   "We'll check by sending a POST request to this URL with a JSON body containing random docs and query."
*   **Error Message:** "Error: Got incorrect matches: Our customer feedback survey revealed that ease of use is a key area for improvement., The infrastructure upgrade includes improvements in data storage and retrieval., The technical documentation for the new product line is now available online."
*   **Function Calling Section:**
    *   "Function Calling (1.5 marks)"
    *   "

---

## Reply 84
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-05T10:57:57.512Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/95

Try sending an api call to openai.

---

## Reply 85
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-05T11:09:12.197Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/96

Check with network tab, you would see the response of api call being made, Compare that with expected output.

Regrading question 8, you would need to check if cors are enabled, check in browser console tab for more.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser window, specifically the developer tools panel. The developer tools are open to the "Network" tab. This tab displays information about network requests made by the web page. On the left side of the browser window, there's a view of the browser's homepage with icons for various websites and a search bar.

**2. Text Content Visible:**

*   **Browser Tabs:**
    *   "My Dashboard - IIT..."
    *   "SOP Link (T12023)"
    *   "Jan 2023 Grading d..."
    *   "Titanic dataset - Go..."
    *   "A (99+) Academia.edu..."
    *   "Mc IIT Madras BS Foun..."
    *   "PE About - Project Euler"
    *   "Other favorites"
*   **Developer Tools:**
    *   "Welcome", " Elements", "Console", "Sources", "Network +"
    *   "Preserve log", "Disable cache", "No throttling"
    *   "Filter", "Invert", "More filters", "All", "Fetch/XHR", "Doc", "CSS", "JS", "Font", "Img", "Media", "Manifest", "WS", "Wasm", "Other"
    *   Timings in milliseconds (1,000 ms to 12,000 ms)
    *   "Name"
    *   Two entries with names like "{ } 1.0?cors=true&content-type=application/x-json-stre...6V%3D4%26LU..."
    *   "Headers", "Payload", "Preview", "Response", "Initiator", "Timing", "Cookies"
    *   Response content: `{"acc":1,"webResult":{}}`
    *   "2 requests", "773 B transferred", "48 B resources"
    *   "Console", "Developer resources", "Network conditions", "Issues", "Performance monitor", "Memory inspector", "Autofill", "Coverage"
    *   "top", "Filter", "Default levels", "33"
*   **Browser Homepage:**

---

## Reply 86
**Author**: Yogaswetha
**Posted**: 2025-02-05T11:09:36.765Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/97

i am unable to find the answer box plss guide me through that

---

## Reply 87
**Author**: Tanmay Garg
**Posted**: 2025-02-05T11:11:56.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/99

You could use AI assistance it helped me.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser window, likely Google Chrome, displaying a Discourse forum page and the Chrome DevTools panel. The forum page appears to be a discussion thread. The DevTools panel is open, showing the "Elements" tab and the "Console" tab, along with the "Styles" pane. There's also an AI assistance panel open at the bottom right.

**2. Text Content:**

*   **Forum Page:**
    *   "Discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/96" (This is the URL of the forum thread)
    *   "22f2001630" (Likely a username or ID)
    *   "Keep getting this error."
    *   "86 / 87" (Likely page numbers)
    *   "23f2000098" (Likely a username or ID)
    *   "you ask for AI assistance, for it helped."
*   **DevTools - Elements Tab:**
    *   ""
    *   ""
    *   "...body.primary-group-ds-students.chat-enabled.category.category-courses-tds-kb.tag-announcement.tag-graded-ass..."
*   **DevTools - Console Tab:**
    *   "Console"
    *   "What's new"
    *   "AI assistance"
*   **DevTools - Styles Pane:**
    *   "Styles"
    *   "Computed"
    *   "Layout"
    *   "Event Listeners"
    *   "@media screen and (max-width: 550px)

---

## Reply 88
**Author**: Sudhish Narayan S
**Posted**: 2025-02-05T11:12:42.808Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/100

Oh OK sure. I will try out and let you know. Thank You!

---

## Reply 89
**Author**: Tanmay Garg
**Posted**: 2025-02-05T11:26:33.292Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/102

Got the answer but it was wired that I had run the curl command three time and the 3 times I got different result.

---

## Reply 90
**Author**: Yogaswetha
**Posted**: 2025-02-05T11:28:20.791Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/103

its not working for me any other options plss??

---

## Reply 91
**Author**: Aashutosh
**Posted**: 2025-02-05T12:51:35.793Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/104

23f2003853:

rm me where I did mistake

Sorry but im facing an issue with question 6 and 7 where its saying load failed when I submit it. when I run the queries locally using curl im getting the expected results.  Any help would be appreciated.

**Image: Screenshot 2025-02-05 at 6.19.41 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or development tool. It appears to be a form or configuration panel where a user is expected to input an API URL. There's an input field for the URL, along with some explanatory text and a "Check" button. An error message is also displayed.

**2. Any text content visible:**

*   "Make sure you enable CORS to allow GET requests from any origin."
*   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
*   "http://127.0.0.1:8001/execute" (This is the user-entered URL in the input field)
*   "TypeError: Load failed"
*   "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."
*   "Check" (on a button)

**3. The context or purpose of what's displayed:**

The UI is designed to allow a user to specify the URL of an API endpoint. The system will then attempt to verify the endpoint by sending a GET request. The purpose is likely to ensure that the API is accessible and functioning correctly. The CORS warning suggests that the application making the request is running on a different origin than the API, and CORS needs to be configured to allow cross-origin requests. The "TypeError: Load failed" message indicates that the system was unable to load or access the specified URL.

**4. Technical details:**

*   The URL "http://127.0.0.1:8001/execute" suggests a local development environment, where the API is running on the user's machine. The port number 8001 is used.
*   The example URL "http://127.0.0.1:8000/execute" shows a similar URL but on port 8000.
*   The text "We'll check by sending a GET request to this URL with ?q=..." indicates

curl "http://127.0.0.1:8001/execute?q=What%20is%20the%20status%20of%20ticket%2083742?"

{"name":"get_ticket_status","arguments":"{\"ticket_id\": 83742}"}

---

## Reply 92
**Author**: Abhigyan Das
**Posted**: 2025-02-05T13:56:17.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/105

For question 2, do we have to make the API call to the proxy or openai? If to the proxy, are there any instructions on the page *before* question 2 that would have pointed me in that direction?

---

## Reply 93
**Author**: Yogaswetha
**Posted**: 2025-02-05T14:04:28.679Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/106

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for testing an API endpoint. It appears to be part of a larger application or learning platform. The UI includes:

*   A JSON snippet defining a function.
*   A form for specifying the API URL and query parameters.
*   A section for displaying the API request and response.
*   A "Check" button, likely for validating the API implementation.

**2. Text Content:**

*   **JSON Snippet:**
    ```json
    {
      "name": "get_ticket_status",
      "arguments": "{\"ticket_id\": 83742}"
    }
    ```
*   **Instructions/Explanations:**
    *   "Make sure you enable CORS to allow GET requests from any origin."
    *   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
    *   "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."
*   **Error Message:**
    *   "SyntaxError: 'undefined' is not valid JSON"
*   **Form Labels/Placeholders:**
    *   "Name"
    *   "Description"
    *   "q *required"
    *   "string (query)"
    *   "What is the status of ticket 83742?"
*   **Buttons:**
    *   "Execute"
    *   "Clear"
    *   "Check"
*   **API Request/Response:**
    *   "Responses"
    *   "Curl"
    *   `curl -X 'GET' \ 'http://127.0.0.1:8000/execute?q=What%20is%20the%20status%20 -H 'accept: application/json'`
    *   "Request URL"
    *   `http://127.0.0.1:80

I am trying this for so long how to fix this plss guide me. thanking you

---

## Reply 94
**Author**: Biray Sursingh Purty
**Posted**: 2025-02-05T14:14:44.787Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/108

there is a problem in question 7 and 8, fast api question, when i click on save, both api calls happens at once at [http://127.0.0.1:8000](http://127.0.0.1:8000/), and i can run fast api app for question 7 or 8 for one only, suppose i check for question 7 it shows correct, also for question 8 i check it shows correct , but when i try to save one of the answer gets incorrected because of simultaneous calls by question 7 and 8 at this address [http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

## Reply 95
**Author**: Khushi Dhankhar
**Posted**: 2025-02-05T14:18:53.764Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/109

**Image: Screenshot 2025-02-05 at 7.44.03 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page, likely part of an online course or assessment. It presents a problem or task related to building a service that finds similar documents based on a user's query. The page includes instructions, a description of the service flow, and a question asking for the API URL endpoint. There's also an input field where the user has entered an answer, and a "Check" button.

**2. Text Content:**

*   **Page Titles:** "My Dashboard - IIT Madras", "Course Introduction :: IITM", "Tools in Data Science", "TDS 2025 Jan GA3 - Large La"
*   **URL:** exam.sanand.workers.dev/tds-2025-01-ga3#hq-get-llm-to-say-yes
*   **Timer/Score:** "04:15:56 left", "Score: 8.5 / 9.5"
*   **Buttons:** "Check all", "Save", "Check"
*   **Service Flow:**
    *   **1. Request Payload:** The client sends a POST request with a JSON body containing:
        *   **docs:** An array of document texts from the internal knowledge base.
        *   **query:** A string representing the user's search query.
    *   **2. Embedding Generation:** For each document in the `docs` array and for the `query` string, the API computes a text embedding using `text-embedding-3-small`.
    *   **3. Similarity Computation:** The API then calculates the cosine similarity between the query embedding and each document embedding. This allows the service to determine which documents best match the intent of the query.
    *   **4. Response Structure:** After ranking the documents by their similarity scores, the API returns the identifiers (or positions) of the three most similar documents. The JSON response might look like this:
        ```json
        {
          "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
        }
        ```
    *   Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 

while saving the 7th,8th question its alteranately getting incorrect

im getting 8.5 marks but while saving it gets deducted to 7 because of these 2 questions

this is really very frustrating since im working on this for so long like 5-8hours but still facing the same issue

what to do

@carlton @s.anand

---

## Reply 96
**Author**: Khushi Dhankhar
**Posted**: 2025-02-05T14:39:36.822Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/110

**Image: Screenshot 2025-02-05 at 8.07.34 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface for a coding assignment or test related to Large Language Models (LLMs). It includes:

*   **Instructions:** A list of instructions for the task.
*   **Code Snippet:** A JSON-formatted code block.
*   **Error Message:** An error message displayed below the code.
*   **UI Elements:** Buttons ("Check", "Check all", "Save"), a score display, and browser tabs.

**2. Any text content visible:**

*   **Browser Tabs:** "My Dashboard - IIT Madras", "Course Introduction :: IITM", "GA3 - Large Language Model", "Tools in Data Science", "TDS 2025 Jan GA3 - Large La"
*   **Instructions:**
    *   "Make sure you pass an Authorization header with dummy API key."
    *   "Use `gpt-4o-mini` as the model."
    *   "The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories."
    *   "The second message must be *exactly* the text contained above."
    *   A paragraph explaining the purpose of the test for DataSentinel Inc.
    *   "Note: This uses a dummy `httpx` library, not the real one. You can only use:"
    *   A list of `httpx` library functions: `httpx.get()`, `httpx.post()`, `response.raise_for_status()`, `response.json()`
*   **Code:**
    *   `DATA = {`
    *   `"model": "gpt-4o-mini",`
    *   `"messages": [`
    *   `{"role": "system", "content": "Analyze the sentiment of the following text as GOOD, BAD, or NEUTRAL."},`
    *   `{"role": "user", "content": "N PIXDC6t EXfymclF e K x1XTpIULdX t6H LTa YGZk,"}`
    *   `]`
    *   `}`
*   **Error Message:** "Error

in the 1st as well both the outouts are exactly same but its still showing error

@carlton

---

## Reply 97
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-05T14:56:42.479Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/111

You can run 2 different severs on different port numbers.

[http://127.0.0.1:8000](http://127.0.0.1:8000) and [http://127.0.0.1:8001](http://127.0.0.1:8001)

---

## Reply 98
**Author**: Sudhish Narayan S
**Posted**: 2025-02-05T15:26:55.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/112

I tried checking the JSON Output in the Networks tab. I am getting error as “Method Not Found”. But, I have allowed POST Method for question 7 as POST method is used in the question. I also tried checking my API by sending a POST request by the same parameters as given by the Website. I  am getting the proper response when I give an API request. Can you please help me out here? I have attached the screenshot  of the error as Picture -1 and the correct output what I get as Picture-2.  Please help me out as I am facing issue for all the API Questions though I am getting the right output. Thank You.

**Image: Screenshot 2025-02-05 205509**
Here's a detailed description of the image:

1.  **What is shown in the image:** The image shows a snippet of JSON code. It appears to be an error response from a web server or API.

2.  **Text content visible:** The JSON object contains a single key-value pair:
    *   `"detail": "Method Not Allowed"`

3.  **Context or purpose of what's displayed:** The JSON snippet indicates that the client made a request to a server using an HTTP method (e.g., GET, POST, PUT, DELETE) that is not supported or allowed for the requested resource. This is a common HTTP error response.

4.  **Technical details:** The code is formatted as a JSON object, enclosed in curly braces `{}`. The key `"detail"` is a string, and the value `"Method Not Allowed"` is also a string. This is a standard way to communicate error information in web APIs. The dark background suggests the code is displayed in a code editor or terminal with a dark theme.

**Image: Screenshot 2025-02-05 205501**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of text, likely from a document or a notification. The text is white against a black background.

**2. Any text content visible:**

The text content reads:

*   "The product update addresses reported bugs and introduces several enhancements."
*   "The Leadership team has approved the expansion of our global IT support network."
*   "The internal..." (the last sentence is incomplete)

**3. The context or purpose of what's displayed:**

The text suggests that it's an announcement or update related to a software product and the company's IT infrastructure. The first sentence highlights bug fixes and improvements in a product update. The second sentence indicates that the leadership team has approved the expansion of the global IT support network. The incomplete third sentence suggests there is more information, but it is cut off.

**4. Technical details:**

There are no technical details visible in the image. It is simply text.

---

## Reply 99
**Author**: Sudhish Narayan S
**Posted**: 2025-02-05T16:00:53.142Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/113

And for Question-9, I tried 80 prompts and I tried every different way, but I am not getting a Yess from the LLM. Can you please say how to proceed for that? Thank You

---

## Reply 100
**Author**: Jayesh Bansal
**Posted**: 2025-02-05T16:22:44.964Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/114

import numpy as np

def most_similar(embeddings):

words = list(embeddings.keys())

dot_product_df = 

for i in words:

for j in words:

dot_product_df.append(np.dot(embeddings[i], embeddings[j]))

return max(dot_product_df)

print(most_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

---

## Reply 101
**Author**: Jayesh Bansal
**Posted**: 2025-02-05T16:23:43.388Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/115

Jayeshbansal:

print(most_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

**Image: image**
Here's a breakdown of the image content:

**1. UI Elements:**

*   **Code Editor:** The image shows a code editor interface, likely within a web application or development environment. The editor has a dark background and contains Python code.
*   **Error Message:** An error message is displayed below the code editor.
*   **Prompt:** The text "Write your Python code here:" is displayed above the code editor.
*   **Scrollbar:** A scrollbar is visible on the right side of the code editor, indicating that the code may extend beyond the visible area.
*   **Warning Icon:** A warning icon (exclamation mark inside a circle) is present in the top right corner of the code editor.

**2. Text Content:**

*   **Code:**
    *   `for i in words:`
    *   `for j in words:`
    *   `dot_product_df.append(np.dot(embeddings[i], embeddings[j]))`
    *   `return max(dot_product_df)`
    *   `print(most_similar({"I experienced issues during checkout.":`
    *   `[-0.10228022187948227, -0.057035524398088455, -0.03200617432594299, -0.1569785177707672, -0.11162916570901871, -0.017878107726573944, -0.06209372356534004, 0.18209508061408997, -0.0027645661029964685, 0.12928052246570587, 0.17609500885009766, -0.1184664517641

---

## Reply 102
**Author**: Jayesh Bansal
**Posted**: 2025-02-05T16:32:18.808Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/116

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** There's a text input field, outlined in red, suggesting an error or validation issue. It contains a URL.
*   **Error Icon:** A red circle with an exclamation mark inside is positioned to the right of the text input field, further indicating an error.
*   **Error Message:** Below the input field, there's an error message displayed in red.

**2. Text Content:**

*   **Question:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
*   **Input URL:** "http://127.0.0.1:8000/execute?q="
*   **Error Message:** "TypeError: Failed to fetch"
*   **Explanation:** "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."

**3. Context and Purpose:**

The image shows a user interface element where a user is expected to input an API URL. The system is validating the URL, and it has encountered an error. The error message "TypeError: Failed to fetch" suggests that the system was unable to connect to the provided URL. The explanation text indicates that the system is attempting to send a GET request to the URL with a query parameter "q" to test the API.

**4. Technical Details:**

*   **API Endpoint:** The example API endpoint provided is "http://127.0.0.1:8000/execute". This suggests a local development environment (127.0.0.1 is the loopback address) running on port 8000.
*   **GET Request:** The system is using a GET request with a query parameter "q" to send a task to the API.
*   **Argument Order:** The system emphasizes that the arguments in the GET request must be in the same order as the function definition in the API. This is important for the API to correctly interpret the request.
*   **"Failed to fetch" Error:** This error typically occurs in JavaScript when a network

---

## Reply 103
**Author**: Arnav Raj 
**Posted**: 2025-02-05T16:34:48.632Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/117

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a split screen with two main sections:

*   **Left Side:** A web browser displaying a question from an online exam or assignment.
*   **Right Side:** A development environment, including a REST client (Thunder Client) and a terminal.

**2. Text Content Visible:**

*   **Exam/Assignment (Left Side):**
    *   "exam.sanand.workers.dev/tds-2025-01-ga3" (URL)
    *   "02:10:25 left" (Time remaining)
    *   "Score: 7 / 9.5"
    *   "Check all" and "Save" buttons
    *   "Here, 'Contents of document 3' is considered the closest match, followed by 'Contents of document 1', then 'Contents of document 2'."
    *   "Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers."
    *   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity"
    *   "http://127.0.0.1:8000/similarity" (Input field)
    *   "Error: Got incorrect matches: The project blueprint for migrating to a microservices architecture is complete., Our system maintenance schedule has been updated to minimize downtime., The IT support portal now features a self-service FAQ for common issues."
    *   "We'll check by sending a POST request to this URL with a JSON body containing random docs and query."
    *   "Check" button
    *   "Function Calling (1.5 marks)"

*   **Thunder Client (Right Side):**
    *   "THUNDER CLIENT"
    *   "New Request"
    *   "POST http://127.0.0.1:8000/similarity"
    *   Tabs: "Query", "Headers", "Auth", "Body", "Tests", "Pre Run"
    *   Body content (JSON):
        ```json
        {
            "docs": ["

@carlton @Jivraj  Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!

I m attaching my codes:

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["OPTION","POST"],  
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def clean_text(text: str):
    """Clean text by lowering case, removing punctuation, and extra spaces."""
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        cleaned_docs = [clean_text(doc) for doc in request.docs]
        cleaned_query = clean_text(request.query)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

        query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

        top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
        matched_docs = [request.docs[i] for i in top_indices]

        return {"matches": matched_docs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
    return {"message": f"Executing query: {q}"}

---

## Reply 104
**Author**: Arulvadivelan V
**Posted**: 2025-02-05T16:48:48.163Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/118

Hi,

I’m sorry if I’m asking an unrelated question, But I’m very confused with the concept of generating the token from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

Could any one suggest the step by step process? I couldn’t able to find that similar question asked by anyone since the conversations are vast.

Please guide me on this. Also do i need to use my personal mail id or iitm mail id for accessing this token

---

## Reply 105
**Author**: Arnav Raj 
**Posted**: 2025-02-05T17:02:48.548Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/119

yes you have to use your IITM email id . Use this link and login you will get your token:

[https://aiproxy.sanand.workers.dev/](https://aiproxy.sanand.workers.dev/)

---

## Reply 106
**Author**: Jayesh Bansal
**Posted**: 2025-02-05T17:51:02.543Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/120

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** There's a text input field, outlined in red, suggesting an error or validation issue.
*   **Error Icon:** A red exclamation mark icon is present on the right side of the input field, further indicating an error.
*   **Prompt Text:** Above the input field, there's a question prompt.
*   **Error Message:** Below the input field, there's an error message displayed in red.

**2. Text Content:**

*   **Prompt:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
*   **Input Field Value:** "http://127.0.0.1:9000/execute"
*   **Error Message:** "SyntaxError: "[object Object]" is not valid JSON"

**3. Context/Purpose:**

The image shows a user interface element where a user is being asked to provide an API URL. The red outline, error icon, and error message indicate that the provided URL or the data associated with it is causing a problem. Specifically, the error message suggests that the system is expecting a valid JSON (JavaScript Object Notation) format, but it's receiving something else, possibly a JavaScript object directly.

**4. Technical Details:**

*   **API URL:** The prompt and the input field value suggest that the user is expected to enter a URL that points to an API endpoint.
*   **Localhost:** The URL "http://127.0.0.1:9000/execute" indicates a local server (localhost) running on port 9000, with an endpoint named "execute".
*   **JSON:** The error message "SyntaxError: "[object Object]" is not valid JSON" implies that the API is expecting data in JSON format, but the data being sent is not valid JSON. This could be due to incorrect formatting, missing quotes, or the presence of a JavaScript object instead of a JSON string.

---

## Reply 107
**Author**: Aditya Kumar Sahu
**Posted**: 2025-02-05T18:28:04.849Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/121

The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to [http://aiproxy.sanand.workers.dev/openai/v1/embeddings](http://aiproxy.sanand.workers.dev/openai/v1/embeddings) with required headers. And, then calculate `similarity_scores` simply using

\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}

which in python syntax is-

np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

---

## Reply 108
**Author**: Sudhish Narayan S
**Posted**: 2025-02-05T18:33:06.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/122

Sir, Regarding the embedding questions, I had posted earlier. Now, I am writing the error I faced. I tried to use the OpenAI API, but I am getting the error as “The Maximum Quota has reached”. I tried using 5 new API Keys from OpenAI, from 5 different accounts. So, I had to use SentenceTransformers, Alibaba gte model. So, as the model has changed, I think so it is expecting answer as got from OpenAI Model, but as I used Alibaba gte model, I am getting different result. Can you please explain how to solve this issue? This will be helpful in my future codes. I could do chat requests but it is not giving output for Embedding requests, I tried it multiple times with multiple different keys.Thank You

**Image: Screenshot 2025-02-05 235804**
Here's a detailed description of the image:

1.  **Content:** The image displays a text-based error message, likely from a software application or API response. The text is formatted as a JSON-like structure.

2.  **Text Content:** The text content is as follows:
    *   `{'error': {'message': 'You exceeded your current quota, please check your plan and billing details.'}`

3.  **Context/Purpose:** The message indicates that the user has exceeded their allowed usage limit (quota) for a particular service or resource. It advises the user to review their subscription plan and billing information. This is a common error message in cloud services, APIs, or any system with usage-based pricing or limitations.

4.  **Technical Details:**
    *   The error message is structured as a dictionary with a key named 'error'.
    *   The 'error' key contains another dictionary with a key named 'message'.
    *   The 'message' key holds the actual error message string.
    *   The use of single quotes suggests that this might be a Python dictionary or a similar data structure.
    *   The black background and white text suggest that this is a screenshot of a terminal or code editor.

---

## Reply 109
**Author**: Sudhish Narayan S
**Posted**: 2025-02-05T18:34:39.598Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/123

This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You

from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class similarity1(BaseModel):
    docs: list[str]
    query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
    docs = similarity1.docs
    query = similarity1.query
    results_docs = model.encode(docs)
    results_query = model.encode(query)
    similarities = {}
    output = []
    for i in range(len(results_docs)):
        c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
        similarities[c] = docs[i]
    k = sorted(list(similarities.keys()))
    for i in k[::-1][:3]:
        output.append(similarities[i])
    return {"matches" : output}
if __name__ == "__main__":
  (uvicorn.run(app))

---

## Reply 110
**Author**: Pururaj Singh Shekhawat
**Posted**: 2025-02-05T18:43:40.732Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/124

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Top Bar:** A red bar at the top indicates the end time of something (likely an assessment or assignment). It also contains the current score, and "Check all" and "Save" buttons.
*   **Question/Discussion Box:** A teal box with a speech bubble icon and text prompting users to join a discussion on Discourse if they have questions.
*   **Login Information:** Text indicating the user is logged in with a specific email address.
*   **Logout Button:** A red "Logout" button.
*   **Recent Saves Section:** A dark green section displaying recent saves, including the date and time of the save, and the score at the time of the save.

**2. Text Content:**

*   "Ended at Wed, 5 Feb, 2025, 11:59 pm IST"
*   "Score: 0"
*   "Check all"
*   "Save"
*   "Have questions? Join the discussion on Discourse"
*   "You are logged in as 24f2005437@ds.study.iitm.ac.in."
*   "Logout"
*   "Recent saves"
*   "Loaded from 5/2/2025, 11:20:33 pm. Score: 6"
*   "Reload from 5/2/2025, 11:20:20 pm. Score: 6"

**3. Context/Purpose:**

The image appears to be a screenshot of a user interface for an online assessment or learning platform. The platform shows that an assessment has ended, displays the user's score, and provides options to check all answers and save progress. It also provides a link to a discussion forum (Discourse) for questions. The user is logged in with a specific email address, and there's a logout button. The "Recent saves" section shows the history of saved progress, including the date, time, and score at each save point.

**4. Technical Details:**

*   The email address "24f2005437@ds.study.iitm.ac.in" suggests the user is affiliated with the Indian

i submitted the assignment on time but i am still getting assignment not submitted. And it also show zero marks. Same thing happened with graded assignment 2. @Jivraj

---

## Reply 111
**Author**: Shouvik Roy 
**Posted**: 2025-02-06T03:04:45.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/125

@Jivraj @carlton

I have submitted ga3 still showing not submitted , why sir?

**Image: Untitled design**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page interface for an online assignment or quiz related to "Large Language Models." It includes UI elements such as:

*   A header with the title "TDS 2025 Jan GA3 - Large Language Models."
*   Instructions for the assignment.
*   A button to "Check all" answers and a "Save" button.
*   A link to a discussion forum ("Join the discussion on Discourse").
*   Information about the logged-in user.
*   A "Recent saves" section.
*   A section for "Module 3: Large Language Models" with details about the assignment.
*   A table showing "Your Score," "Peer Average," and "Median Score."

**2. Text Content:**

Here's a breakdown of the key text content:

*   **Title:** "TDS 2025 Jan GA3 - Large Language Models"
*   **Instructions:** A numbered list of instructions, including:
    *   "Learn what you need."
    *   "Check answers regularly by pressing Check."
    *   "Save regularly by pressing Save."
    *   "Reloading is OK."
    *   "Browser may struggle."
    *   "Use anything."
    *   "It's hackable."
    *   "Note: You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."
*   **Link:** "Have questions? Join the discussion on Discourse"
*   **User Information:** "You are logged in as 23f1001348@ds.study.iitm.ac.in."
*   **Recent Saves:** "Reload from 2/4/2025, 4:04:47 PM. Score: 9.5"
*   **Module Information:**
    *   "Module 3: Large Language Models"
    *   "Assignment"
    *   "Graded Assignment 3"
    *   "Assessment (Due: 5 Feb 2025)"
    *   "Not Submitted"
*   **Score Table:**
    *   "Your Score"

---

## Reply 112
**Author**: Shouvik Roy 
**Posted**: 2025-02-06T03:08:19.006Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/126

@Jivraj @carlton

please reply why its showing not submitted in ga3 but i have submitted that

**Image: Untitled design**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page interface for an online assignment or quiz related to "Large Language Models." It includes UI elements like buttons, text instructions, score displays, and assignment details.

**2. Text Content:**

*   **Title:** "TDS 2025 Jan GA3 - Large Language Models"
*   **Instructions:** A numbered list of instructions for the assignment, including:
    *   "Learn what you need."
    *   "Check answers regularly by pressing Check."
    *   "Save regularly by pressing Save."
    *   "Reloading is OK."
    *   "Browser may struggle."
    *   "Use anything."
    *   "It's hackable."
*   **Note:** "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."
*   **Question Prompt:** "Have questions? Join the discussion on Discourse"
*   **Login Information:** "You are logged in as 23f1001348@ds.study.iitm.ac.in."
*   **Logout:** Logout
*   **Recent Saves:** "Reload from 2/4/2025, 4:04:47 PM. Score: 9.5"
*   **Module Title:** "Module 3: Large Language Models"
*   **Assignment:**
    *   "Graded Assignment 3"
    *   "Assessment (Due: 5 Feb 2025)"
    *   "Not Submitted"
*   **Score Headers:** "Your Score," "Peer Average," "Median Score"
*   **Score Values:** "-" for all score types.

**3. Context and Purpose:**

The page is likely part of an online learning platform or course management system. The purpose is to provide students with instructions, access to an assignment (Graded Assignment 3), and information about their score and submission status. The instructions suggest a flexible and open approach to the assignment, even allowing the use of external resources and hacking the code.

**4. Technical Details:**

*   The page is likely rendered using HTML, CSS, and JavaScript.
*   The presence of

---

## Reply 113
**Author**: Srividhya
**Posted**: 2025-01-30T10:42:26.627Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/127

@carlton, @Jivraj

Both the api based questions i am unable to get the output it always says bad request

**Image: Screenshot 2025-01-30 at 3.55.56 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code editor, likely VS Code or a similar IDE. The editor is displaying a Python file named `main.py`. There's a file explorer on the left, the code editor in the center, and a terminal/output panel at the bottom.  There's also a smaller panel on the right, showing terminal options.

**2. Text Content:**

*   **File Explorer:**
    *   `GA3_Q8` (Project Name)
    *   `app` (Directory)
    *   `_pycache_` (Directory)
    *   `__init__.py` (Python file)
    *   `main.py` (Python file - currently open in the editor)
    *   `venv` (Directory - likely a virtual environment)
    *   `.env` (Environment file)
    *   `requirements.txt` (File listing dependencies)

*   **Code Editor (main.py):**
    *   `def parse_query(query: str):` (Function definition)
    *   `return "get_ticket_status", {"ticket_id": int(match_ticket_status.group(1))}`
    *   `# Match "Arrange meeting 2025-12-17, 06:09, room: Conf1"` (Comment)
    *   `match_schedule_meeting = re.match(...)` (Regular expression matching)
    *   `r"(?i)(arrange\s*meeting|schedule\s*a\s*meeting)\s*(?:on\s*)?(\d{4}-\d{2}-\d{2}..."` (Regular expression pattern)
    *   `if match_schedule_meeting:` (Conditional statement)
    *   `print(f"Schedule Meeting Match: {match_schedule_meeting.groups()}") # Debug log` (Print statement for debugging)
    *   `return "schedule_meeting", { ... }` (Return statement with a dictionary)
    *   `"date": match_schedule_meeting.group(2),`
    *   `"time": match_schedule_meeting.group(3),`

**Image: Screenshot 2025-01-30 at 3.57.17 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface, likely for an online coding assessment or assignment. It includes UI elements such as:

*   A header with the due date, score, "Check" and "Save" buttons.
*   A code snippet displayed in a text box.
*   An input field for entering a URL.
*   An error message.
*   A question or task description.

**2. Any text content visible:**

*   **Header:** "Due Sun, 2 Feb, 2025, 11:59 pm IST", "Score: 6.5 / 9.5", "Check", "Save", "Finish update"
*   **Code Snippet:**
    ```json
    {
      "name": "get_ticket_status",
      "arguments": "{\"ticket_id\": 83742}"
    }
    ```
*   **Instructions/Context:** "Make sure you enable CORS to allow GET requests from any origin.", "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute"
*   **URL Input Field:** "http://127.0.0.1:8000/execute"
*   **Error Message:** "Error: Failed to fetch: Bad Request"
*   **Further Explanation:** "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."
*   **Task/Question:** "Get an LLM to say Yes (1 mark)"

**3. The context or purpose of what's displayed:**

The image depicts a coding challenge or assignment where the user needs to implement an API endpoint. The task involves:

*   Creating an API that can handle GET requests.
*   Ensuring CORS (Cross-Origin Resource Sharing) is enabled.
*   Providing the correct API URL.
*   The system will test the API by sending a GET request with a query parameter `q`.
*   The user needs to get an LLM to say "

all other questions i have finished. even in Ga2 all these api and flask creates a lot of issues. if there is any complete guide to understand this also pls help us.

---

## Reply 114
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-30T22:22:09.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/128

Hi @23ds1000022 ,

Check network tab, there check for response of `http://127.0.0.1:8000/api` request.

---

## Reply 115
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-01T12:44:20.471Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/129

I have counted the number of tokens in gpt-4o-mini but when I was entering the answer in portal it was showing incorrect please take a look and provide a solution for it .

**Image: Screenshot 2025-02-01 180627**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element from the OpenAI Platform. It appears to be a text input area or a playground where users can interact with different GPT models. The UI includes:

*   **Model Selection Tabs:** Tabs at the top allow the user to select between different GPT models: "GPT-4o & GPT-4o mini", "GPT-3.5 & GPT-4", and "GPT-3 (Legacy)".
*   **Text Input Area:** A large text area contains a string of seemingly random characters, numbers, and some recognizable words. A scrollbar indicates that the content is longer than what's currently visible.
*   **Buttons:** Two buttons are present below the text area: "Clear" and "Show example".
*   **Token and Character Count:** At the bottom, the UI displays the number of "Tokens" (406) and "Characters" (625) in the text area.
*   **OpenAI Platform Header:** The top of the image shows the "OpenAI Platform" logo and links to "Docs" and "API reference".

**2. Text Content Visible:**

*   **Header:** "OpenAI Platform", "Docs", "API reference"
*   **Model Selection Tabs:** "GPT-4o & GPT-4o mini", "GPT-3.5 & GPT-4", "GPT-3 (Legacy)"
*   **Text Area Content:** The text area contains a long string of text, including:
    *   "List only the valid English words from these: ..." (This suggests the text area is used to filter or validate words.)
    *   A long list of strings like "eWHNetl", "eGEjb", "9", "kZFurXr", "Pnti2d0", "HnV66V0", "cR9zhYBi", "NL", "9T1DU3", "DaRw", "9irI10", "6AiKKkHU", "FJ7XYuT", "ZBfU30", "TH", "B", "EuaXvr4VYp", "YC", "li6J4dJPn", "pTWN", "EZshp", "e

---

## Reply 116
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-01T16:06:29.936Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/130

There are few more tokens for the user prompt, I think if you add 7 or 8 then you would get correct answer.

Other way to do this question is send a request to anand sir’s aiproxy and in response you will get number of input tokens.

---

## Reply 117
**Author**: Sakthivel S
**Posted**: 2025-02-01T16:32:58.809Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/131

I inspected the JavaScript code of this website, I saw that the answer took my input and added 7 to it, why is it programmed this way? Even if I were to use the AI proxy that was given shouldn’t the number of tokens remain unaffected?

---

## Reply 118
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-01T17:03:51.869Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/132

When you send request to openai through anand sir’s proxy it takes some tokens for user prompt.

When you use tokenizer from openai’s webpage then it doesn’t take care of that.

---

## Reply 119
**Author**: Dwarakesh
**Posted**: 2025-02-03T18:11:42.650Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/133

How to answer the 3rd question in ga 3 i have to no clue (tired inspecting its html pages)

---

## Reply 120
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-03T22:25:44.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/134

[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

      [](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

[2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

---

## Reply 121
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-03T19:44:12.086Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/135

Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

Q7 & Q8 in these questions the problem is the same my app couldn’t fetch the details from the file.

`from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Add CORSMiddleware with more restrictive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only this specific origin
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],  # Allow only POST and OPTIONS methods
    allow_headers=["Content-Type", "Authorization"],  # Allow only specific headers
)

# OpenAI API key (use your own key)
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDY3NDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tMJtqZrzRqREY7E3wsFMd9PkElXEbRBpCkb533ORGEU'

# Request body model for /similarity endpoint
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Function to get embeddings (using OpenAI API)
def get_embedding(text: str):
    response = openai.Embedding.create(
        model="text-embedding-ada-003",  # Use the correct model
        input=text
    )
    return response['data'][0]['embedding']

# POST /similarity endpoint
@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    docs = request.docs
    query = request.query
    query_embedding = get_embedding(query)
    doc_embeddings = [get_embedding(doc) for doc in docs]
    
    # Cosine similarity
    similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
    ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]
    
    return JSONResponse(content={"matches": ranked_docs[:3]})

# Optionally, handle requests to the root (GET /)
@app.get("/")
async def root():
    return {"message": "Welcome to the similarity API!"}
`

and for Q8

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def get_ticket_status(ticket_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "balance": 1000.0}

def calculate_performance_bonus(employee_id: int, current_year: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}

def report_office_issue(issue_code: int, department: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"issue_code": issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -> Dict[str, Any]:
    """Extract parameters from the query string."""
    # Convert the query to lowercase for case-insensitive matching
    query = query.strip().lower()

    if match := re.match(r"what is the status of ticket (\d+)\?", query):
        return {
            "name": "get_ticket_status",
            "arguments": {"ticket_id": int(match.group(1))}
        }
    elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
        return {
            "name": "schedule_meeting",
            "arguments": {
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            }
        }
    elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
        return {
            "name": "get_expense_balance",
            "arguments": {"employee_id": int(match.group(1))}
        }
    elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
        return {
            "name": "calculate_performance_bonus",
            "arguments": {
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            }
        }
    elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
        return {
            "name": "report_office_issue",
            "arguments": {
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            }
        }
    return {}

@app.get("/execute")
async def execute_query(q: str):
    # Extract the function name and arguments from the query
    result = extract_parameters(q)
    
    if not result:
        return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)
    
    # Call the respective function
    func_name = result["name"]
    arguments = result["arguments"]
    
    # Call the function dynamically based on func_name
    if func_name == "get_ticket_status":
        response = get_ticket_status(**arguments)
    elif func_name == "schedule_meeting":
        response = schedule_meeting(**arguments)
    elif func_name == "get_expense_balance":
        response = get_expense_balance(**arguments)
    elif func_name == "calculate_performance_bonus":
        response = calculate_performance_bonus(**arguments)
    elif func_name == "report_office_issue":
        response = report_office_issue(**arguments)
    
    # Return the response in the requested format
    return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)

Please kindly guide me with these problems as I am trying to do it since last 3 days. I am exhaust now, Please help me with this. @Jivraj , @carlton , @Saransh_Saini

---

## Reply 122
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-03T22:40:49.588Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/136

Hi Sakshi

 Sakshi6479:

Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

      [drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

      [](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

[2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

For question 7

 Sakshi6479:

import openai

You won’t be able to send request through openai python module, here is one example how you would make a request

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
    'model':'gpt-4o-mini',
    'messages':[
        {
            'role':'user',
            'content':'What is 2+2?'
        }
    ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)

You would need to use professor Anand’s proxy or some other api key through which request can be made.

Url’s for free api keys:

[AI Proxy](https://aiproxy.sanand.workers.dev/)
[OpenAI GPT-4o · GitHub Models](https://github.com/marketplace/models/azure-openai/gpt-4o/playground)

The way to use api’s is demonstrated in live sessions, also refer to this documentation [sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy).

For question 8, you’ll need to use OpenAI’s function calling feature and identify which function needs to be called and arguments to be used, we discussed in last Friday’s session on functions like `order` and `cancel_order`.

Kind regards

---

## Reply 123
**Author**: Shalini Saravanan
**Posted**: 2025-02-03T09:24:00.805Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/137

Hello sir,

While working on this question, I’m encountering this problem. It looks like the request is being made successfully (and I verified it by a POST request via Postman ), however while submitting my URL at the assignment portal, I’m getting an error.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal output or console log. It displays information about a process that involves resetting a collection, creating a new collection, adding documents to a database, and searching for similar content based on a query. The output also includes HTTP request information.

**2. Any text content visible:**

The text content includes:

*   `INFO: 127.0.0.1:59423 - "OPTIONS /similarity HTTP/1.1" 200 OK`
*   `Collection reset successfully!`
*   `Created new collection: documents`
*   `Added 10 new documents to the database.`
*   `Searching for query: How is our internal training addressing cybersecurity challenges?`
*   `Found matches: ['Employee training on cybersecurity best practices is being rolled out company-wide.', 'The staff handbook has been updated to reflect current operational policies.', 'Our quality assurance team has implemented automated testing protocols.']`
*   `INFO: 127.0.0.1:59423 - "POST /similarity HTTP/1.1" 200 OK`

**3. The context or purpose of what's displayed:**

The output suggests a system or application is performing a similarity search on a collection of documents. The process involves:

*   **Resetting a collection:**  This likely clears any existing data.
*   **Creating a new collection:** A new collection named "documents" is created.
*   **Adding documents:** 10 new documents are added to the database.
*   **Searching for similar content:** A query is executed to find documents similar to "How is our internal training addressing cybersecurity challenges?".
*   **Displaying matches:** The system finds three matches related to employee training, staff handbooks, and quality assurance protocols.

The "OPTIONS" and "POST" lines with the `/similarity` endpoint suggest that this is part of a web API or service that handles similarity searches. The `200 OK` indicates successful HTTP requests.

**4. Technical details:**

*   **IP Address and Port:** `127.0.0.1:59423` indicates the process is running on the local machine (localhost) on

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** There's a text input field outlined in red, suggesting an error or warning state.
*   **Information Icon:** To the right of the input field, there's a red circle with an exclamation mark inside, further indicating an issue.
*   **Prompt Text:** Above the input field, there's a question prompting the user to enter an API URL endpoint.
*   **Error Message:** Below the input field, there's an error message.

**2. Text Content:**

*   **Prompt:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity"
*   **Input Field Value:** "http://127.0.0.1:8000/similarity"
*   **Error Message:** "Error: Got incorrect matches. Employee training on cybersecurity best practices is being rolled out company-wide. The staff handbook has been updated to reflect current operational policies. Our quality assurance team has implemented automated testing protocols."

**3. Context and Purpose:**

The image shows a UI element where a user is being asked to provide an API URL. The red outline and the information icon suggest that the provided URL is not valid or causing an error. The error message below indicates that the input is not producing the expected results, possibly related to incorrect data matching. The error message also contains unrelated information about employee training and company policies, which is likely a placeholder or a generic error message that needs to be more specific.

**4. Technical Details:**

*   The API URL example and the input field value use "127.0.0.1," which is the local loopback address, often used for development or testing.
*   The port number "8000" is a common port for development servers.
*   The "/similarity" part of the URL likely refers to a specific endpoint or resource related to similarity calculations or comparisons.
*   The error message suggests that the API is intended to find matches, but the input is not producing the correct matches.

I even tried deploying on a public URL using render. My guess is there is a formatting issue or it’s not sorting correctly based on the similarity score and not returning the top 3.

Would appreciate if I can get some clarity on the same

Thanks and Regards

Shalini

---

## Reply 124
**Author**: SHAON BALLAV
**Posted**: 2025-02-03T22:26:57.365Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/138

Hello, I think the format of the response body should be like: { “matches” : [ “ABC”, “ABC”, “ABC”]}. I think it is because of your formatting issue.

**Image: Screenshot_20250204_032923**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows the user interface of Postman, a popular API client. It displays a request being made to a local server. The UI elements include:

*   **Request Method and URL:** A dropdown menu set to "POST" and a URL field containing "http://127.0.0.1:8000/similarity".
*   **Tabs:** Tabs for "Params", "Authorization", "Headers (8)", "Body", "Scripts", and "Settings". The "Authorization" tab is currently selected.
*   **Authorization Details:** The "Auth Type" is set to "No Auth".
*   **Response Body:** The response body is displayed in JSON format.
*   **Status Code and Response Time:** A "200 OK" status code is shown, along with a response time of "17.26 s" and a size of "232 B".
*   **Toolbar:** A toolbar with icons for saving, sharing, code generation, and other actions.

**2. Text Content:**

*   **URL:** "http://127.0.0.1:8000/similarity"
*   **Request Method:** "POST"
*   **Tabs:** "Params", "Authorization", "Headers (8)", "Body", "Scripts", "Settings", "Cookies"
*   **Authorization:** "Auth Type", "No Auth", "No Auth", "This request does not use any authorization."
*   **Response Body:**
    *   `"matches": [`
    *   `"FastAPI is great for APIs."`
    *   `"Embedding models improve NLP."`
    *   `"Machine learning is evolving."`
    *   `]`
*   **Status:** "200 OK", "17.26 s", "232 B"
*   **Other UI elements:** "Save", "Share", "Send", "Preview", "Visualize"

**3. Context and Purpose:**

The image shows a user making a POST request to a local API endpoint ("http://127.0.0.1:8000/similarity"). The API likely performs some kind of similarity analysis or matching, as

I had used (well gpt) the below two decorators to format:

class SearchRequest(BaseModel):
    docs: List[str]  # The list of documents to search through
    query: str       # The search query string

class SearchResponse(BaseModel):
    matches: List[str]  # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)

.........

return SearchResponse(matches=sorted_matches[:3])

It basically checks the Request  and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that  :grinning:

---

## Reply 125
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-03T22:45:02.248Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/139

{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}

Check if your response is in this format.

kind regards

Jivraj

---

## Reply 126
**Author**: Matlin Jeleshiya 
**Posted**: 2025-02-05T18:48:31.180Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/140

Does the final submission get graded, or is the highest-scoring submission considered?

I’m facing an issue where my score dropped from 8 to 6.5 when I checked all the answers one last time before submitting. I suspect the drop is due to the 3rd and 7th questions.

**Image: Screenshot 2025-02-06 001446**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a UI element, specifically a list of recent save files. Each entry in the list shows a "Reload" button, the date and time the save was created, and a score associated with that save. The background is a dark green color.

**2. Any text content visible:**

*   **Title:** "Recent saves"
*   **Button Label:** "Reload" (appears multiple times)
*   **Save Information:**
    *   "from 2/5/2025, 11:59:18 PM. Score: 6.5"
    *   "from 2/5/2025, 11:30:37 PM. Score: 8"
    *   "from 2/5/2025, 10:44:08 PM. Score: 6.5"

**3. The context or purpose of what's displayed:**

The UI element is likely part of a game or application that allows users to save their progress. The "Recent saves" list provides a way for users to quickly reload a previous save point. The date, time, and score information help the user choose the appropriate save to reload.

**4. Technical details:**

*   The UI uses buttons labeled "Reload" to trigger the loading of a specific save file.
*   The date and time format is "month/day/year, hour:minute:second AM/PM".
*   The score is represented as a floating-point number.
*   The UI is designed with a dark theme.

---

## Reply 127
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T06:05:01.971Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/141

**Image: Screenshot 2025-02-06 at 11.27.07 am**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a webpage, likely a quiz or exam interface. It includes a header with administrative information, a title, an "Instructions" section, and a set of instructions for the user. There are also cartoon eyes.

**2. Text Content:**

*   **Header:** "[Admin] Ended at Wed, 5 Feb, 2025, 11:59 pm IST Score: 0 Check all Save"
*   **Title:** "TDS 2025 Jan GA3 - Large Language M"
*   **Instructions:** (Numbered list)
    1.  "Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure.)"
    2.  "Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times."
    3.  "Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated."
    4.  "Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters."
    5.  "Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser."
    6.  "Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want."
    7.  "It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed."
*   **Note:** "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."

**3. Context and Purpose:**

The image displays the instructions for an online quiz or exam, specifically "TDS 2025 Jan GA3 - Large Language M". The instructions provide guidance to the user on how to approach the quiz, including saving answers, checking answers, and what resources are allowed. The instructions are unusually permissive, explicitly allowing the use of external resources like the internet, ChatGPT, and even hacking the quiz code.

**4. Technical Details:**

*   The header indicates

The score drops because some questions may require you to either keep a server turned on or some dynamic changes may occur for some questions (The dynamic changes are intentional in some questions, in order to get students to learn by doing. So if you solved everything and the score is the maximum… just make that your last submission. The score you see is the score you will get for your last submission).

If you want check a question without submitting. Then just use the check button instead. But your last submission is whats scored.

---

## Reply 128
**Author**: Pururaj Singh Shekhawat
**Posted**: 2025-02-06T07:21:52.633Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/142

Same problem with my submission

---

## Reply 129
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T14:43:17.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/143

**Image: Screenshot 2025-02-06 at 8.11.15 pm**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a bar chart visualizing the distribution of GA3 active scores. The chart has the following elements:

*   **X-axis:** Represents the scores, divided into ranges (0, 10], (10, 20], (20, 30], (30, 40], (40, 50], (50, 60], (60, 70], (70, 80], (80, 90], and (90, 100].
*   **Y-axis:** Represents the GA2 student count, ranging from 0 to 250.
*   **Bars:** Each bar corresponds to a score range and its height indicates the number of students within that range. The bars are colored in blue.
*   **Data Labels:** Each bar has a number above it, indicating the exact student count for that score range.
*   **Title:** "GA3 Active Score Distribution"

**2. Any text content visible:**

*   **Title:** "GA3 Active Score Distribution"
*   **X-axis label:** "Scores"
*   **Y-axis label:** "GA2 Student Count"
*   **Score ranges:** 0, (0, 10], (10, 20], (20, 30], (30, 40], (40, 50], (50, 60], (60, 70], (70, 80], (80, 90], (90, 100]
*   **Student counts:** 12, 42, 49, 62, 55, 59, 93, 104, 91, 35, 249
*   **Legend:** (90, 100], ga3 student count: 249

**3. The context or purpose of what's displayed:**

The chart aims to show how students performed on GA3, grouped by score ranges. It provides a visual representation of the distribution of scores, highlighting which score ranges had the most

For those that are interested.

---

## Reply 130
**Author**: Ayush Kumar Shaw 
**Posted**: 2025-02-08T01:44:42.024Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/144

sir why the GA marks is not being reflected in the course page. We are getting a sign of non submission.

Is there any way getting the score.

---

## Reply 131
**Author**: Shahil Khan
**Posted**: 2025-02-09T15:16:04.343Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/147

Hello sir ,I find a issue with submission of GA4.  Actually i submitted ga3 on “[Technical Assessment](https://exam.sanand.workers.dev/tds-2025-01-ga3)”        with full marks but in the course >grade portal it is saying it is not submitted. what’s the issue is this?

---

## Reply 132
**Author**: Imran Ashraf
**Posted**: 2025-02-10T20:31:27.549Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/148

I also have same problem

---

## Reply 133
**Author**: Andrew David
**Posted**: 2025-02-11T18:55:49.596Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/149

can you please reply?

@Jivraj @carlton

---

## Reply 134
**Author**: Carlton D'Silva
**Posted**: 2025-02-16T06:31:21.790Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/150

A post was merged into an existing topic: [GRADED ASSIGNMENT RESULT NOT SHOWING , kindly check on this](/t/graded-assignment-result-not-showing-kindly-check-on-this/166816/20)

---

## Reply 135
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-16T04:40:57.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/151

*No content*

---

## Reply 136
**Author**: SHAIK YASIR HAMEED
**Posted**: 2025-05-24T17:22:55.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/152

Error: Invalid promptfooconfig.yaml: Missing required assertion for: [https://api.github.com/orgs/](https://api.github.com/orgs/)

for 14th Question

# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
  - file://prompt.json

providers:
  - openai:gpt-4o-mini
  - openai:gpt-4o-mini
  - openrouter:openai/gpt-4o-mini
  - openrouter:openai/gpt-4.1-nano
  - openrouter:google/gemini-2.0-flash-lite-001
  - openai:gpt-4o-mini

defaultTest:
  vars:
    system_message: file://system_message.txt
    previous_messages:
      - user: Who founded Facebook?
      - assistant: Mark Zuckerberg
      - user: What's his favorite food?
      - assistant: Pizza

tests:
  - vars:
      question: Did he create any other companies?
  - vars:
      question: What is his role at Internet.org?
  - vars:
      question: Will he let me borrow $5?
  - vars:
      question: Did he create any other houses?
  - vars:
      question: Did he create any other hospitals?
  - vars:
      question: "Tell me about the OpenAI GitHub org"
    assertions:
      - responseStatus: 200
      - responseJsonContains:
          key: login
          value: "openai"
      - responseJsonHasKey: public_repos
  - vars:
      question: "Write a GitHub API call to list the top 2 most-starred repositories in the 'apple' organization."
    assertions:
      - contains-all:
          values:
            - "https://api.github.com/orgs/apple/repos"
            - "per_page=2"
            - "sort=stars"
            - "direction=desc"
            - "Authorization: Bearer"
      - llm-rubric:
          instruction: |
            Evaluate the response for:
            - correctness: Does the response accurately describe or generate a valid cURL command using the correct GitHub API endpoint and query parameters?
            - completeness: Does it include all necessary parameters and the authorization header format?
          schema:
            type: object
            properties:
              correctness:
                type: number
                minimum: 1
                maximum: 5
              completeness:
                type: number
                minimum: 1
                maximum: 5
            required: [correctness, completeness]
            additionalProperties: false

  # ✅ Required assertion related to https://api.github.com/orgs/
  - vars:
      question: "What does https://api.github.com/orgs/ return?"
    assertions:
      - contains: "https://api.github.com/orgs/"

---

## Reply 137
**Author**: Tanmay
**Posted**: 2025-05-28T12:10:33.577Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/155

Question 4:

I am trying this :

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image."},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,iVBORw0KGgoAAAANS.......=" }
        }
      ]
    }
  ]
}

I am getting this error :

Error: The image_url.url must be the base64 data URL of the image

I verified that my Base64 encoding for the image is correct ..

---

## Reply 138
**Author**: Ajit
**Posted**: 2025-05-29T08:28:21.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/156

Getting the same issue -

# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 18 most-starred repositories
    from the "stripe" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting/limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/stripe/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=18'
        name: "Limits to 18 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "stripe"
          - Limits results to exactly 18 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder
        name: "LLM rubric: task compliance" ```

---

## Reply 139
**Author**: Puneet Bajaj
**Posted**: 2025-05-29T15:59:44.618Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/158

Try this - right click on image and click open in new tab, in the new tab you will see the base64 url of image in chrome tab url bar

Hope this helps

---

## Reply 140
**Author**: Shiva varshney 
**Posted**: 2025-05-30T08:32:40.341Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/159

**Realizing the Value of Collaboration**

As I’ve been going through this course, one thing that’s really started to make sense to me is how important collaboration is. None of us can know everything — and that’s okay. We all have different strengths, and when we work together, especially on projects, those strengths really start to shine.

I’ve come to believe that collaboration isn’t just about dividing tasks, it’s about learning from each other, supporting one another, and finding smarter ways to solve problems as a team. It helps us get things done more effectively and on time, and honestly, it makes the whole learning process a lot more enjoyable.

This course is definitely helping me build that mindset, and I’m excited to keep growing through shared learning.

if somebody feels the same  then Reply , Thankyou

---
