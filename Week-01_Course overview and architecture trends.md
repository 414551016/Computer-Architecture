# Week-01_Course overview and architecture trends.md
Date：2026-09-08(二)
教學資源：

## 0 分鐘 3 秒0:03
offered by the Computer Science Department. And today there will be two parts. So the first part I will talk about what is computer architecture. And then the second part will be on the course logistics, including like the grading requirements and like if you want to add course, what's the policy and stuff like that. Okay.
> 本課程由計算機科學系開設。今天的安排分為兩部分：第一部分我將介紹什麼是電腦體系結構；第二部分則講解課程的相關安排，包括評分要求以及選課（如加選課程）的政策等。好的。
- **計算機結構（Computer Architecture）**是研究電腦硬體如何設計、運作及協同處理資料的學科，核心目標是在效能、成本與功耗之間取得最佳平衡。
  <br>它主要探討 CPU、記憶體、輸入輸出設備及匯流排之間如何協同工作，以有效執行程式。<br>其重要內容包含：指令集架構（ISA）、資料路徑設計、控制單元、快取記憶體（Cache）、流水線（Pipeline）、平行處理、多核心處理器及記憶體階層等。
  <br>從軟硬體關係來看，計算機結構是連結作業系統、編譯器與硬體平台的基礎，使程式能轉換為機器指令並由 CPU 執行。因此，計算機結構不僅是資訊科學的重要基礎，更是設計高效能電腦、嵌入式系統、AI運算平台與現代網路設備的核心知識。

## @1 0 分鐘 22 秒
And...
@1 0 分鐘 24 秒
Typically all the lectures will be recorded, so if you don't want to come, it's totally fine. Okay, yeah.
> 通常所有講座都會錄影，所以如果你不想來，完全沒問題。好的，沒問題。

## 1 0 分鐘 35 秒
OK, so to start with, how is computer architecture? So, from the broadest definition, the architecture is kind of the design of the abstraction, or we say the implementation layers like that allow us to execute the applications to the manufacturing technologies. So, I mean, this sentence is long, but...
> 好的，首先我們來談談電腦體系結構。從最廣泛的定義來看，體系結構可以被理解為一種抽象設計——或者說是建構了從應用程式到製造技術之間各個實現層級的設計。這句話雖然有點長，但…

## @1 0 分鐘 55 秒
To explain it in the easiest way is that, for example, the application would be like you want to talk to the chat bot, like you talk to the GPT, talk to the cloud, or you want to watch videos online, you want to play video games or whatever. There are a lot of applications you want to achieve. And then the physics and technology is like how you learn in the physics course, like there are particles.

## @1 1 分鐘 15 秒
in this world and their electrons and stuff like that. But there's a huge gap between that, right? Even though you know the rule or the characteristics of the electrons or the particles, that does not allow you to start to watch videos on YouTube. So the gap is really large to bridge in the one step. So in the architecture course, we try to discuss the different abstraction layers that enable this to happen.

## @1 1 分鐘 37 秒
So to use an easy example to illustrate how each step works, let's use the example of the sorting. So typically, I think sorting is used as an example in many different courses, but assume that we want to sort an array of the numbers. So sorry, the application sounds a little bit stupid, but anyway.

## @1 1 分鐘 58 秒
So you have an array of numbers and you want to sort them. And then the next thing, like in your undergrad, you have the algorithm course, you probably discuss many different ways of sorting that. So for example, like the quick sort, the bubble sort, and you discuss the complexity, so how hard it is to implement this algorithm. And also,

## @1 2 分鐘 17 秒
If you do a lot of implementation, you also discuss, for example, how much memory you will need to realize this application. So, in this, in here, we...

## @1 2 分鐘 29 秒
Sorry.

## @1 45 分鐘 28 秒
And then on the integrity and the responsible AI use. So basically the labs are designed to develop your own problem solving skill. And I know that everyone use AI to support your learning, but you should not replace it because be careful on the AI usage. I think it's really risky if you rely on AI too much because you are sacrifice your own capability.

## @1 45 分鐘 50 秒
Or the chance to learn to learn, right? Because if you use everything with AI, then maybe after a semester you won't get a lot from from this course, but but just but just a grade. OK, but you need to check adapt and make make it your own. I think the most important, you are fully responsible for all the assignments you submit, so the work that lacks original.

## @1 46 分鐘 11 秒
originality, either you copy from your friend, lab mate, or you share an AI account, whatever. As long as we sync, identify as a plagiarism, you will get penalized. Yeah, sorry, I need to avoid further.

## @1 46 分鐘 30 秒
argument. I want to be clear up front. So we actually we do check if the assignments are too similar to each other and no matter how you how you get that, if the words that we think that lacks the originality, you may get point detection or up to even failing the course. I want you to be clear on that. I want to be clear on that.

## @1 46 分鐘 52 秒
Okay, and then there's no public sharing of the labs. So for example, trying to post the stuff on GitHub or Google Drive, or I mean public sharing, if you just keep it on your private repo or your own Google Drive is fine, but please try not to share that because...

## @1 47 分鐘 9 秒
Yeah, I think that's kind of like the intellectual property between the T of the core staff. So I hope, I mean, I have no, I cannot force you not to do that. So I kindly ask you not to, yeah. And but if we find it during the semester, yeah, I think we are clear on the policy. So please.

## @1 47 分鐘 30 秒
If we find, if we find a public copy of the lab during the semester, you may get some penalty as well. Yeah, so I hope that we respect each other. Yeah, and...

## @1 47 分鐘 43 秒
To make sure that we follow the course policy and also the integrity rules. OK, and if you don't feel comfortable with these rules, you are, I mean...

## @1 47 分鐘 54 秒
We with you still have two weeks to decide, right? If you are, you want to stay in this course, OK?

## @1 48 分鐘 1 秒
And then just a little bit, this is the first year I tried to show the statistics, but anyway, I know many students want to know about that. So I think last year, this year, the course is particularly large, and I don't know why, because the system makes the upper bound higher, I think. In the past, it was like for 90 students, and typically after the

## @1 48 分鐘 20 秒
course adding period is maybe a little bit more than 100 or something like that. And then a lot of students drop in the middle of the semester due to many different reasons. And I think if you try to write a lab and you found that this is not a course for you, many students will decide to drop in the middle. Okay, so last year, last fall, 78 students last year, the end of the semester, and you can see that

## @1 48 分鐘 44 秒
If you are a grad student, I think...

## @1 48 分鐘 48 秒
You need me to be here, I to pass.

## @1 48 分鐘 51 秒
Am I correct?

## @1 48 分鐘 53 秒
I don't know. Yeah, I think B minus is 70. Yeah. So if you are a grad student, then you need to be here to pass. And then if you are like an undergrad, then I think the bar is lower. Okay. So we can see that most people pass. It's not a big issue. But for this course, we probably, we have much more A than A plus.

## @1 49 分鐘 13 秒
So if you really aim for like an A, you probably need to spend substantial effort in the lab to make sure that you get most of the, not only the benchmark pass, but also like a good performance. So I just want to make that clear. So this is not the course, like 50% of the students will get an A. If that's your expectation, then this is not.

## @1 49 分鐘 35 秒
the right place. Yeah, sorry. Because I mean, a lot of students will come later on and then try to make a lot of arguments. So I want to set the expectation and also that he is feel tired afterwards. So I just try to set the expectation right. I think testing the course is definitely, I won't say you will need to pay some effort, but definitely not that hard. Because I mean,

## @1 49 分鐘 55 秒
Some of students just forget to drop, like they never show up, right, even in the exams. So this, yeah, but even if you pay some effort, I don't think it is that hard, but just that if you want to get like an outstanding score or grade in this course, you probably need to focus a lot on the labs and also the exams. Okay.

## @1 50 分鐘 14 秒
So that's the statistics from the last year. And yeah, so the selection process is that everyone needs to register in the system, no matter if you fill out the form or not. I mean, if you fill out the form, please also register your register in the system for the random lottery.

## @1 50 分鐘 34 秒
in the system. Because in my experience, many people go back home, open E3, and download Lab Zero and see they need to install a lot of tools and write very long, and then they decide to drop. So actually, even though there are many people who want to add the course, but typically there's also a fair amount of people will drop the course. So I think there's still like a reasonable chance that you can actually go through the random artery to get added.

## @1 50 分鐘 58 秒
Okay, so yeah, just we will close the form soon after the class ends, so please try to fill out the form now. Okay.

## @1 51 分鐘 7 秒
And we don't.

## @1 51 分鐘 9 秒
We don't need to collect any documents. If you get selected, we will go.

## @1 51 分鐘 14 秒
The time or go to the by the department office directly, so we don't need the, ohh, we don't need that.

## @1 51 分鐘 23 秒
We don't need that paper, OK?

## @1 51 分鐘 25 秒
And then, if you, we will send you an e-mail if you get added by this process, and...

## @1 51 分鐘 33 秒
Sorry. Because I cannot guarantee that how many students will be added, because it will also depend on how many students drop the course, right? So, I mean, the results will be out before, at the latest, before the class next week, but we probably will add some students like on the rolling base, depends on the status of the whole.

## @1 51 分鐘 54 秒
that the whole student amount. So yeah, I think that's the last slide page I have. Does anyone have any questions?

## @1 52 分鐘 6 秒
Oh, sorry, that's not that's not that page. I have two more. Sorry, but what's wrong with this? Sorry.

## @1 52 分鐘 15 秒
No.

## @1 52 分鐘 20 秒
That's annoying. OK, anyway, I will just, I will just continue, just ignore that sound. I'm sorry. So, just a quick try to quickly differentiate what's the difference between this course and the undergrad computer organization. So, this is the photo of the RISC one set in five.

## @1 52 分鐘 39 秒
Micron at most, and run as a one.

## @1 52 分鐘 44 秒
Megahertz. OK, so this is also one of the first first view is at risk, and this roughly like 50,000 transistor.
















