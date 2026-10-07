# Generative AI in User Experience Design and Research: How Do UX Practitioners, Teams, and Companies Use GenAI in Industry?

| [Macy Takaffoli](https://orcid.org/0009-0006-2561-801X) | [Sijia Li](https://orcid.org/0009-0000-7260-862X) | [Ville Mäkelä](https://orcid.org/0000-0001-6095-2570) |
| --- | --- | --- |
| University of Waterloo | University of Waterloo | University of Waterloo |
| Waterloo, Canada | Waterloo, Canada | Waterloo, Canada |
| mtakaffoli@uwaterloo.ca | k287li@uwaterloo.ca | ville.makela@uwaterloo.ca |

### ABSTRACT

User Experience (UX) practitioners, like UX designers and researchers, have begun to adopt Generative Artificial Intelligence (GenAI) tools into their work practices. However, we lack an understanding of how UX practitioners, UX teams, and companies actually utilize GenAI and what challenges they face. We conducted interviews with 24 UX practitioners from multiple companies and countries, with varying roles and seniority. Our findings include: 1) There is a significant lack of GenAI company policies, with companies informally advising caution or leaving the responsibility to individ- ual employees; 2) UX teams lack team-wide GenAI practices. UX practitioners typically use GenAI individually, favoring writing- based tasks, but note limitations for design-focused activities, like wireframing and prototyping; 3) UX practitioners call for better training on GenAI to enhance their abilities to generate effective prompts and evaluate output quality. Based on our findings, we provide recommendations for GenAI integration in the UX sector.

### CCS CONCEPTS

• Computing methodologies → Artificial intelligence; • Human- centered computing → Empirical studies in HCI; HCI theory, concepts and models.

### KEYWORDS

Generative Artificial Intelligence, GenAI, Industry Practices, User Experience Design, User Experience Research, Company Policies, Human-AI Collaboration, Interaction Design

## ACM Reference Format:

Macy Takaffoli, Sijia Li, and Ville Mäkelä. 2024. Generative AI in User Experience Design and Research: How Do UX Practitioners, Teams, and Companies Use GenAI in Industry?. In Designing Interactive Systems Confer- ence (DIS ’24), July 01–05, 2024, IT University of Copenhagen, Denmark. ACM, [New York, NY, USA, 15 pages. https://doi.org/10.1145/3643834.3660720](https://doi.org/10.1145/3643834.3660720)

### 1 INTRODUCTION

User experience (UX) plays a pivotal role in creating successful digital products [30, 59]. The design and development of these products typically follows a user-centered approach, which includes

a wealth of activities like user research, requirements definition,

[This work is licensed under a Creative Commons Attribution-NonCommercial International 4.0 License.](https://creativecommons.org/licenses/by-nc/4.0/)

DIS ’24, July 01–05, 2024, IT University of Copenhagen, Denmark

© 2024 Copyright held by the owner/author(s).

ACM ISBN 979-8-4007-0583-0/24/07

[https://doi.org/10.1145/3643834.3660720](https://doi.org/10.1145/3643834.3660720)

brainstorming, wireframing, graphic design, prototyping, and user testing. UX practitioners, including UX designers, user interface (UI) designers, UX researchers, and other roles associated with UX, can have diverse skill sets and often contribute to different activities or steps while working closely together with other UX experts [11]. UX practitioners have been interested in leveraging artificial intelligence (AI) and machine learning (ML) in their work prac- tices for years [1, 14, 31, 91]. Current research has proposed that adopting AI into UX design, and into human-computer interaction (HCI) practices more generally, can bring many benefits. Some such benefits include fostering creativity [9], automating mundane tasks [14 ], improving the scalability of design processes [75], support- ing decision-making [3, 14 ] and human-human collaboration [63], and speeding up and optimizing activities like sketching [21, 35], wireframing [68], and usability and user testing [22, 23].

Now, with the recent wave of Generative Artificial Intelligence (GenAI) and tools like ChatGPT<sup>1</sup>, Midjourney<sup>2</sup>, and DALL-E<sup>3</sup>, many industries are looking to adopt them widely. According to a recent survey, companies see GenAI as the most transformative technology in a generation, with 90% of the surveyed companies increasing their investments in GenAI [79 ]. UX practitioners are especially looking to adopt GenAI tools in their work [e.g., 26, 67, 74, 82 ], likely because many UX activities involve producing text and images.

However, we currently lack an understanding of how UX praciti- tioners in the industry are actually using GenAI, and what policies and practices have been developed in companies and their UX teams. We argue that this understanding is crucial for developing efficient and responsible GenAI-enhanced UX practices. While prior work has looked into AI-related industry practices before [e.g., 14, 46, 84], there is not much research on how GenAI has been adopted into UX processes [66 ], especially at the company and team level. We argue that an investigation is needed due to the recent, massive wave of GenAI that is currently shaping many industries<sup>4</sup>.

Therefore, in this work, we aim to understand the processes, attitudes, and challenges of GenAI use in the UX sector. Our primary research questions were:

• RQ1: How are companies allowing GenAI use in their UX departments and what policies are in place?

• RQ2: How are UX practitioners and UX teams integrating GenAI into their work practices?

• RQ3: What are the current challenges and needs regarding the integration of GenAI into UX industry practices?

1[https://chat.openai.com/](https://chat.openai.com/)

2[https://www.midjourney.com/](https://www.midjourney.com/)

3[https://openai.com/dall-e-3](https://openai.com/dall-e-3)

4GenAI has existed for a much longer time, but in the context of this paper, we refer

to the most recent wave of GenAI, including text generation tools like ChatGPT, and

image generation tools like DALL-E and Midjourney.

![image](image_001.png)

To this end, we conducted online interviews with 24 industry UX professionals. To ensure rich insights and the inclusion of different perspectives, we recruited participants from various backgrounds. Participants came from eight different countries, had varying levels of seniority, and served in different UX-related roles, including de- signers, researchers, and managers. All participants were employed by different companies, and we included companies ranging from start-ups and small businesses to large corporations.

Using qualitative content analysis, we identified 10 themes which we categorized under three major dimensions: GenAI Policies and Adoption in Companies (RQ1), GenAI Adoption and Practices in UX (RQ2), and Challenges and Needs Regarding GenAI in UX (RQ3). Our main findings include: 1) There is a significant lack of formal company policies regarding GenAI, with companies informally ad- vising caution or leaving the responsibility to individual employees,

2) There is a significant lack of team-level practices and collabora- tion in UX teams. Individually, UX practitioners report using GenAI widely for research-focused tasks, but commonly note limitations for design-focused activities, like wireframing, prototyping, and graphic design, and 3) UX practitioners identify challenges with writing effective GenAI prompts and assessing output quality, and voice concerns about other practitioners over-relying on GenAI. UX practitioners call for GenAI training, and request better support in GenAI tools for UX design. Based on our findings, we provide recommendations to UX practitioners, teams, and companies.

Through our engagement with industry experts, our work pro- vides an overview on the current status of GenAI integration in the UX sector, highlights the challenges and needs that UX practition- ers have regarding GenAI, and provides recommendations for the adoption of GenAI.

### 2 RELATED WORK

In this section, we review relevant existing research surrounding AI, GenAI, and UX. To understand the context and scope of our work, it is important to understand the difference between design for AI and design with AI. We review both of these concepts below; however, our work focuses on design with AI. Then, we review research that has made direct enquiries to UX practitioners about AI integration. We finish by identifying gaps in current research.

### 2.1 UX Practices for AI: How UX Can Improve

### AI-Enhanced Products

By "designing for AI" we refer to practices, research, and tools where the target of the design—the product—has an AI component. There is widespread interest in the research community to investigate how we can design for and foster human-AI collaboration and AI-enhanced products [ 85], and businesses worldwide are looking to utilize GenAI tools like ChatGPT in their products [34 , 37 ]. It is widely recognized that AI should be human-centered [81], and that UX and HCI are needed to create responsible, explainable, trustworthy, and usable AI systems [45, 77 , 78], especially because there are risks and concerns about AI among workers [76] and the public [69]. As a result, prior research has discussed the challenges relating to designing AI-enhanced systems [83, 85], proposed AI design guidelines and principles [4, 57], and proposed tools and methods to help designers understand AI capabilities [86].

### 2.2 UX Practices with AI: How AI Can Improve

### UX and HCI Practices

By "designing with AI" we refer to practices, research, and tools where the process of design has an AI component. AI is expected to fundamentally change the way we design things [25]. The HCI community has been actively exploring how AI, HCI, and UX come together, evidenced by a wealth of studies, opinion pieces, and work- shops on the topic [e.g., 26, 53 , 54, 64, 66, 67 , 74, 82]). Researchers have proposed and created AI-enhanced tools to aid UX profession- als, as well as proposed and evaluated AI-enhanced processes and methods, which we review next.

Prior work has built several AI tools and computational models for UX-related tasks. Much of this work focuses on design activities, including AI-based ideation [36], sketching and drawing [16, 35, 55], wireframing [10 , 24], graphic design [90], layout optimization [17, 68], and prototyping [ 44, 50]. Other AI tools have been proposed to assist with research tasks, like analyzing usability test videos [23] and think-aloud sessions [22], recognizing the user’s emotional state during usability evaluations [60], and automatically detecting design violations in graphical user interfaces Moran et al. [51].

With a focus not on specific tools but on processes and methods, researchers have studied how AI can be integrated into UX activi- ties. Abbas et al. [1] surveyed existing literature on how machine learning is utilized in user experience design, and Dave et al. [15] conducted a survey on AI-based approaches to turn UI mockups into wireframes and prototypes, and such approaches have reported good results [6, 61]. Other work in this area has explored using AI/ML to, among other things, assist in creating design proposals [13 ], serve as a collaborative partner to foster self-reflection [73] and creativity [32] among designers, generate personas [5, 33 , 62], and communicate data analysis findings to UX researchers [39].

Recently, some research has surfaced focusing on GenAI and ChatGTP. Tholander and Jonsson [67] explored how GPT 3 can be integrated into co-creative design processes for ideation and rapid sketching. Similarly, Al-sa’di and Miller [2] investigated the integration of GenAI tools, specifically ChatGPT 3.5, into the Design Thinking process.

### 2.3 AI Practices and Policies in Industry

While plenty of studies have recruited UX practitioners as their study participants, for example, to receive feedback on their pro- posed AI/ML tools or practices, there are—to our knowledge—only a handful of studies that have enquired about the UX professionals’ actual, adopted industry practices regarding AI or ML.

Liao et al. [46] interviewed 20 UX practitioners who were work- ing on AI products about explainable AI (XAI), contributing to the design of XAI. Similarly, Yang et al. [84] interviewed 13 UX design- ers who designed products that were utilizing ML, contributing to the design on ML-enhanced products. Chromik et al. [14] sur- veyed practitioners experienced in UX, ML, or both to understand how data-driven ML techniques could support their work. Dove et al. [19] surveyed UX practitioners to understand how ML could be used as a design material. Yildirim et al. [87] investigated how practitioners use the People + AI Guidebook [58] when designing AI-enhanced products.

Closest to our work is the research conducted by Lu et al. [48] and Li et al. [43]. Lu et al. [48] conducted a study with 8 UX profes- sionals in 2021 to understand how AI/ML could support their design practices. They identified lacking support for activities that involve more "design thinking", such as user interviews and user testing. In- terestingly, they also discovered that AI tools at the time generated outputs that UX professionals deemed too generic, without consid- ering the designer’s specific domain or the company’s style. Most recently, Li et al. [43] interviewed 20 UX designers, focusing on the designers’ individual perceptions and practices regarding GenAI. The designers believed that GenAI can enhance productivity and serve as an assistive tool to help with repetitive and generic tasks. However, designers also expressed concern over skill degradation and potential unemployment among junior designers. Overall, Li et al. [43] highlight the importance of integrating GenAI into UX design practices due to its expected impact on the industry.

### 2.4 Summary and Research Gap

In the realm of designing with AI, existing research has proposed a wealth of tools and practices for UX activities, like brainstorming [e.g., 13, 67 ], sketching and drawing, [e.g., 35, 55], wireframing and prototyping [e.g., 10 , 44, 50 , 68], and user testing and analysis [e.g., 23, 39]. While much of this research has had promising results, they are merely proposed ways to work with AI; we do not know if and how these tools and methods are used in the industry. There is surprisingly little research on actual AI-supported UX industry practices. Existing research in this area, even if fairly recent, has mostly focused on other types of AI/ML and not GenAI [e.g., 14 , 31, 91], and almost exclusively focused on individual practices [ 43, 48]. Hence, based on our literature review, we can identify two major gaps in existing research:

• Research Gap #1: There is very little research on GenAI- specific UX practices in the industry. So far, we are only aware of Li et al. [43] who have investigated UX industry practices regarding recent GenAI tools like ChatGPT. How- ever, they focused on UX designers and their perceptions of GenAI; there is need to explore UX practices more broadly and cover a wider variety of UX roles.

• Research Gap #2: We are not aware of any research on team-level and company-level practices, discussions, and policies regarding the adoption and use of AI/GenAI in UX industry practices. This is especially important because AI can have a significant impact on team settings [89 ], and impacts entire companies and industries [66].

With these remarks and research gaps in mind, we planned an online interview study with UX practitioners, where we enquired about not only the participants’ individual practices and attitudes, but also about their company’s policies and communication as well as the practices and discussions among their teams.

### 3 ONLINE INTERVIEW STUDY

To answer our RQs, we conducted an online interview study with 24 participants, all of whom worked professionally with UX. The study was approved by our institution’s research ethics board.

### 3.1 Study Design

We chose to conduct our research through a semi-structured in- terview, as opposed to, for example, an online survey for multiple reasons. Interviews can yield exceptionally in-depth results from each participant, and they allow for flexibility; the interviewer can probe new topics on the spot based on the participant’s responses whenever the need arises [42 ]. Moreover, our research was qual- itative and consisted of a large number of open-ended questions; online surveys are typically not suitable for such enquiries, leading to high drop-out rates and low-quality responses [52]. Finally, due to the nature of our enquiry (e.g., relating to company policies and attitudes), we hypothesized that our participants would be more comfortable providing such details directly to a researcher as opposed to typing their answers into a survey.

We furthermore chose to conduct our interviews online, because it allowed us to reach out to UX practitioners worldwide and re- cruit a diverse sample of participants. We describe our recruitment strategies in the subsection below.

We designed our interview questions based on our review of ex- isting literature and identified research gaps, as well as our research questions. In addition to demographic questions, we included ques- tions about topics like their work team and their role in the team, company-level and team-level policies and discussions regarding AI, specific AI tools and practices and changes in workflow, and perceived strengths and weaknesses of AI in UX. The full list of interview questions is provided in Appendix A.

Our study and all of its materials were reviewed by our insti- tution’s research ethics board (REB). Once we acquired approval from the REB, we began recruiting participants.

### 3.2 Participants and Recruitment

We identified potentially suitable participants via LinkedIn and by reaching out to companies in multiple countries. Participants were eligible for our study if they 1) were at least 18 years old, 2) worked in the industry in a role related to UX, and 3) had completed at least one UX industry project. We invited individuals for the interview via email. Prospective participants could sign up for the interview by choosing a 60-minute time slot via Calendly<sup>5</sup>, which automatically created a Teams meeting for the chosen time slot.

An overview of the participants’ demographics is provided in Table 1. Our sample consisted of 24 participants (7 women, 17 men), with an average age of 36 (Min = 23, Max = 47). One participant had a high school diploma (4%), one had a bootcamp diploma (4%), eight participants had a Bachelor’s degree (33%), nine had a Master’s degree (38%), and five had a PhD (21%).

The participants had varying roles as follows: UX Researcher (8, 33%), UX Designer (6, 25%), Head of UX (3, 13%), Product De- signer (2, 8%), Product Design Manager (2, 8%), UX Writer (1, 4%), Chief Product Officer (1, 4%), and Assistant VP of UX (1, 4%). The participants’ experience in the field ranged from 1 year to 25 years. 22 participant (92%) had permanent full-time jobs, one participant was an external contractor at a company, and one participant was a freelancer. The companies our participants represented ranged from very small companies and startups (1–10 employees) to inter- national corporations (over 10000 employees).

5[https://calendly.com/](https://calendly.com/)

DIS ’24, July 01–05, 2024, IT University of Copenhagen, Denmark Macy Takaffoli, Sijia Li, and Ville Mäkelä Gender & Country Age Group Title Years in industry Company size Male 17 (71%) 18 to 19 years 0 (0%) UX Researcher 8 (34%) 1–2 6 (25%) 1–10 4 (17%) Female 7 (29%) 20 to 24 years 3 (13%) UX Designer 6 (25%) 3–4 3 (13%) 10–100 0 (0%) 25 to 29 years 1 (4%) Head of UX Design 3 (13%) 5–6 4 (17%) 100–500 6 (25%) Canada 11 (46%) 30 to 34 years 6 (25%) Product Designer 2 (8%) 7–8 2 (8%) 500–1000 2 (8%) USA 4 (17%) 35 to 39 years 6 (25%) Product Design Manager 2 (8%) 9–10 4 (17%) 1000–5000 2 (8%) Finland 3 (13%) 40 to 44 years 7 (29%) UX Writer 1 (4%) 10+ 5 (20%) 5000–10000 4 (17%) Iran 2 (8%) 45 to 49 years 1 (4%) Chief Product Officer 1 (4%) 10000+ 6 (25%) Bangladesh 1 (4%) Assistant VP of UX Design 1 (4%) Italy 1 (4%) Pakistan 1 (4%) Germany 1 (4%)

Table 1: Summary of participant demographics.

### 3.3 Procedure

Prior to the online interview, the participants were informed about the overall goals of the research through an information letter sent to them via email.

At the beginning of the interview and after greeting the intervie- wee, they were informed that participation is voluntary, and they may decide to end the session at any time. We also emphasized that they could choose to skip questions for any reason. Then, based on the information letter sent to them in advance, we verbally asked them to confirm their eligibility, and then asked them to confirm their consent to participation in the interview, the recording of the interview, later analysis of their data, as well as the use of anony- mous quotes in publications. Once participants agreed, we began the recording and proceeded with the interview.

We started the interview with demographic questions, an overview of which was presented in Table 1. After the demographic questions, we enquired about their company and team, like which industries their projects focused on, the size of their team, and their role within the team. Then, we enquired about company-level and team-level policies and discussions regarding AI, like whether there were any restrictions in place, if there were concerns or hesitation, what kinds of other policies were in place, and if and how AI was discussed in the company and within the team.

Next, we enquired about their specific AI practices, like which tools they use, for what kinds of tasks, how AI has changed their workflow, and then enquired about their attitudes, like level of trust in AI. We also asked how their use of AI potentially different from their colleagues, and what kinds of practices and AI use they had observed from others. In case the participant reported that they nor their team used any AI tools, we diverted to ask a different subset of questions at this point, which centered around their reasons for not using any AI tools and what would need to change for them to adopt AI into their work.

Finally, we asked the participants to list what they thought the strengths and weaknesses of AI in UX practices were, and asked them to specify any needs or recommendations that might help them use AI more effectively in the future.

At the end, we thanked the participants for their time and valu- able insights. The interviews lasted for an average of 60 minutes. Participants were compensated with a Tango gift card (value around

22.5 USD), sent to them via email after the interview was completed.

### 3.4 Qualitative Content Analysis

Our main interview questions consisted of open-ended questions. We conducted an analysis of the participants’ responses with three researchers using qualitative content analysis (QCA) [72]. QCA is a method similar to thematic analysis, both of which consist of researchers familiarizing themselves with the data, and generating codes and themes via an iterative process [72 ]. While thematic analysis can be seen as a more interpretivist approach focused on developing nuanced themes, in QCA, themes can be more descrip- tive in nature and researchers give more meaning to the frequency of codes when developing themes [71 ]. To support this process, we utilized the collaborative tool Jamboard <sup>6</sup> .

In the next section, we present our results in detail.

### 4 RESULTS

Our results are divided into the themes identified during our analy- sis, which are further categorized into three dimensions. An overview of the dimensions and themes is presented in Table 2.

### 4.1 GenAI Policies and Adoption in Companies (RQ1)

4.1.1 Theme 1.1: Lack of formal GenAI policies in companies. We identified a significant lack of formal policies among the intervie- wees’ employers. Most participants noted that there were no formal policies, guidelines, or even emails or discussions from manage- ment or higher-ups regarding GenAI. Most of these participants noted that it was a "personal decision" (P2) left to the individual: "It’s a personal choice at this moment. [My company]

is not providing us anything in terms of tools. That

hasn’t been a conversation yet.” (P8)

Some reported high-level remarks by team managers or other parties regarding GenAI use (e.g., "be cautious with data"), hinting at the vague and informal nature of these communications. Some reported that a certain level of caution was simply "expected" in the company culture, even though there was no clear communication about GenAI. On rare occasions, though, participants noted that policies were being set up or they were being discussed among the upper management, but the employees did not know anything yet.

6[https://jamboard.google.com/](https://jamboard.google.com/)

<table>
<tr><th colspan="2">1. GenAI Policies and Adoption in Companies (RQ1)</th></tr>
<tr><td>Theme 1.1:</td><td>Lack of formal AI policies in companies</td></tr>
<tr><td>Theme 1.2:</td><td>Current GenAI policies and measures in companies</td></tr>
<tr><td>Theme 1.3:</td><td>Cautiousness about GenAI in large companies</td></tr>
</table>

## 2. GenAI Adoption and Practices in UX (RQ2)

Theme 2.1: Lack of team-level GenAI practices and discussions Theme 2.2: GenAI in research-focused vs. design-focused tasks Theme 2.3: Common uses and tools for GenAI

<table>
<tr><th colspan="2">3. Challenges and Needs Regarding GenAI in UX (RQ3)</th></tr>
<tr><td>Theme 3.1:</td><td>Quality and correctness of output</td></tr>
<tr><td>Theme 3.2:</td><td>Dependency on AI</td></tr>
<tr><td>Theme 3.3:</td><td>Need for GenAI training</td></tr>
</table>

Theme 3.4: Improvement of GenAI for design-focused activities

Table 2: Overview of dimensions and themes discovered from the interview data using qualitative content analysis.

Several participants reported that specific GenAI tools were blocked in their company, and some of them had built their own GenAI tools, or licensed commercial tools for privacy reasons: "With ChatGPT launched a year ago, within a couple

of weeks, there was a note that said [ChatGPT] was

blocked from all corporate machines [...]” (P3)

"We can’t access [the main ChatGPT with OpenAI]

from a work computer [...] It’s blocked. We are using

a licensed copy of ChatGPT which is not connected

to the data we feed into it. It doesn’t train the open

AI model.” (P6)

Participants consistently highlighted their individual sense of responsibility, professionalism, and judgment. They noted, for ex- ample, that despite the lack of company policies, they "knew better" than to insert sensitive data into an external GenAI tool. Two par- ticipants stated:

“When experimenting with AI, we needed to pay at-

tention to not share any personal information of our customers or any sensitive company information” (P2)

"GPT is not restricted in our company and I am not

aware [of] any policies, but as a professional, I know

not to share confidential data with chatbots." (P24)

4.1.2 Theme 1.2: Current GenAI policies and measures in companies. Those participants that reported any existing policies or actions by the company regarding GenAI use were almost exclusively moti- vated by, and centered around, data privacy. These included things like building their internal GenAI tools to ensure data privacy and security (and to enable the use of company data with GenAI), providing guidelines or "best practices" for GenAI use especially regarding what data is allowed to be included, setting up a ded- icated governance team to oversee AI use within the company, relaying rules and restrictions via communication channels (e.g.,

Slack) and in-person meetings, internal training on privacy mea- sures and GenAI use, as well as recent policies focusing on client safety, data collection, and data storage.

4.1.3 Theme 1.3: Cautiousness and Data Privacy Concerns about GenAI. Many participants talked about data privacy concerns in their company, potential conflicts between AI and their current policy statements, and how AI can result in "intellectual property breaches" (P2), which also led to much longer approval processes: "[GenAI] is labeled higher risk. It’s already taken

pretty much the year for [GenAI tools] to go through

the regulatory process. But now, because it’s at high

risk, they’re going through even more.” (P16)

“We are expected to keep user information confiden-

tial. We cannot adopt [GenAI] because it’s not part

of our policy statements and data privacy. So general

policies all apply [on GenAI].” (P9)

"Asking for an AI tool in [my] company, usually takes

more time than regular tools, since it needs to go

through security and legal terms to be approved in ad-

dition to the regular process which involves checking

the requirements and budget." (P6)

It is also worth noting that the industry in which the company was involved in likely played a role in the level of caution. The most notable restrictions were reported by participants’ whose employers were in finance and banking. One of them mentioned:

"I think the number one concern for the implemen-

tation of AI in any company is privacy and security.

And that gets multiplied by 10 when you’re talking

about a financial company. The company wants to

make sure that it’s due diligence to the highest level

before the implementation of any [AI tools].” (P17)

In the same vein, one participant mentioned that their company’s engagement with AI was in its infancy, and any actions and discus- sions about GenAI were "driven by individual initiatives rather than structured directives by the company" (P7). This, again, hints at the individual responsibilities of employees rather than structured efforts by companies.

Some participants noted working around these restrictions by using GenAI tools at home. Such participants noted, though, that they strictly used GenAI for activities like preparing drafts and presentations, which did not involve sensitive details about the company or their clients, hinting again at their individual sense of responsibility. One participant explained:

"GPT is restricted in the company, but I do some

generic work like creating drafts, summaries, and

emails with this tool on my personal computer." (P16)

Participants representing small startups generally reported a more relaxed attitude, saying that "we are very open to using AI tools, and my boss is always impressed with the output" (P12) and"we don’t have any policy around AI because we are a very tiny startup” (P18). Another participant working for a startup mentioned that their company is interested in experimenting with more AI tools "since they like to increase productivity" (P10).

### 4.2 GenAI Adoption and Practices in UX (RQ2)

4.2.1 Theme 2.1: Lack of team-level GenAI practices and discussions. We noted a significant lack of discussions and practices regarding GenAI among teams, teammates, and supervisors. Some partici- pants directly reported that they do not discuss the matter:

"We never talk with my coworkers about AI tools

policies, but we are all aware of how to use them

and not to share any sensitive data. [...] We don’t

communicate how the team achieves the outcome;

as long as they care about confidential and sensitive

information and the outcome is acceptable." (P24)

"We haven’t openly discussed with the team that how

they use AI and what tools they are using." (P11)

"GPT is popular [in the team], but we don’t openly

talk with coworkers that GPT edits this work. [...] I

don’t think my manager has any problem with me

using it." (P14)

“I’m not sure about my coworkers [...] because we

usually don’t talk about this topic at work. I just know

they are using some AI tools in their work process,

but no more details.” (P10)

In other cases, the lack of team-level practices was highlighted by the participants’ inability to talk clearly about their team members’ practices, resulting in speculation or vague remarks. When asked about whether their team members are using GenAI, for example, one participant said "I assume they are" (P7), another said "I don’t know about my coworkers, they might use [GenAI], but we haven’t talked." (P21), and a third said "It is mostly on an individual basis, so people just kind of adopt them where they see fit" (P9). Some participants were provided sgeneral or vague comments on their teams or colleagues’ GenAI adoption, for example that "the design team is using [GenAI] plugins in Figma" (P11), and "my coworkers use some visual tools for image generation" (P20).

4.2.2 Theme 2.2: GenAI in research-focused vs. design-focused tasks. We identified a trend where UX practitioners working in more research-focused roles reported more comprehensive use of GenAI than those working more exclusively on design-related tasks.

In design-focused areas, participants reported using GenAI com- monly in the early stages, like brainstorming and iteration and presenting their ideas to others (e.g., using Midjourney to generate visual representations of ideas), to speed up their work and develop ideas. Some designers also reported using GenAI for specific tasks like "Adobe Firefly for creating icons" (P15).

That said, many designers stated that they had tried to use GenAI tools for further, perhaps more advanced areas of their work, but that they did not find the current tools mature and helpful enough: "It feels to me that the AI design tools aren’t quite ca-

pable of creating something that is meaningful enough.

[My] design work relates to challenges about very spe-

cific technical things instead of [the product] being

just a website or something. [...] I have used [com-

putational methods] for something in the past, like

algorithms that create color schemes, but it is often

the case that the challenges we face are much more

complex than that." (P1)

“[I was] using Midjourney for designing a banner, but

it didn’t work that well. And I guess our prompts

weren’t good enough. But it was good for ideation,

not for the complete work.” (P5)

In contrast, GenAI was much more widely used in research-focused tasks, like designing studies, generating drafts, formatting and analyzing data, and summarizing results and prior research. Generally, participants perceived GenAI to be more mature in these areas. For example, participants reported using GenAI for "doc- umentation" (P12), to "help with UX writing" (P22), to "come up with interview questions" (P6, P10), and to "reframe study ques- tions" (P21). Another participant said that "GPT is really helpful for summarizing articles and find related work" (P17). One participant explained what they did with GenAI:

"We did user research and we documented all of our

[data] into Miro and then had the Miro AI create sum-

maries and findings based on [data]. And it worked

very well. There was one obvious factual error [in

the findings], so you can’t like simply trust it, but

overall it did a very good job and also helped us in

the creation of the report." (P1)

4.2.3 Theme 2.3: Common uses and tools for GenAI. In our study, ChatGPT was the most popular GenAI tool, mentioned by every participant during the interview. Regardless of a participant’s posi- tion level and exact role, everyone reported using (or having used) ChatGPT in their personal lives and work routines on some level.

In addition to ChatGPT, in the area of research, participants men- tioned using Copilot, Grammarly, and AI transcription software like Otter and Fireflies in their work routines. In the area of design, UX designers, graphic designers, and content designers relied on im- age generation tools like MidJourney, Adobe Firefly, and Microsoft Designer. Furthermore, participants highlighted that generative AI features have been gradually integrated into designers’ commonly used software, such as Figma, Photoshop, Adobe Illustrator, and Adobe XD, either as plugins or new features within the software.

We identified the most common tasks for which our participants used GenAI. The majority of related statements were provided in the context of research-focused activities (as pointed out in Theme 2.2), although some were focused on design activities, and some were more general in nature. Many relevant quotes have been provided in the previous themes; we build on them briefly here.

Summarizing content. UX practitioners commonly used GenAI to summarize various types of content. This included, for example, "summarizing meeting notes" (P8, P22), "summarizing articles and giving a human answer" (P7), or more generally "summarizing or simplifing texts" (P19), and "summarizing information" (P6).

Brainstorming and visualization. Participants reported brain- storming and ideation as a common use for GenAI. One participant said that GenAI was akin to "quickly brainstorming with someone" (P12), and another said that “[GenAI] allows a good conversation starter for especially the brainstorming side of things” (P6). One participant praised image-generation tools like MidJourney and Microsoft Designer specifically for their "fast iteration" of ideas (P10). Another participant also mentioned that "Midjourney is good for ideation, not for completing the whole work” (P5).

Writing and creating drafts. UX practitioners commonly re- ported usign GenAI to assist with writing, especially in creating the "first draft" (P1), while also noting that it did not do all the work:

“In the beginning of projects, I use [GPT] pretty ex-

tensively to create the first draft of something. [...] It

often requires revision, but it saves me from that first

step of actually writing, the first [version]." (P6)

"It’s helped me along in the [writing] process, but it

hasn’t helped me all the way to the end." (P7)

Data analysis. UX researchers commonly used GenAI to ana- lyze data and identify common findings. One participant mentioned that they "had the Miro AI create summaries and findings based on [data]" (P1), and another said that they sometimes used it to "syn- thesize data" (P3). Another participant explained more thoroughly: “It was like 75 open ended survey responses and I

[...] strip them of [the participant number] and dump

them into ChatGPT, and asked [ChatGPT] to generate

5 insights based on the 75 responses.” (P6).

Being an assistant. GenAI was commonly described as a gen- eral "assistant" that completes various specific and sometimes te- dious tasks, often answering a serendipitous need like "finding good alternative words for a presentation" (P7), "framing things and helping organize your mind" (P11), and similarly, "helping work through the things I’m thinking through" (P6).

### 4.3 Challenges and Needs Regarding GenAI Use in UX (RQ3)

4.3.1 Quality and correctness of output. UX practitioners were critical of GenAI’s ability to produce accurate content, saying that GenAI "just comes up with stuff without support" (P14), has "glaring errors" (P3), and "has bias in its data analysis results" (P21). One participant highlighted concerns about AI bias on a deeper level:

“There are a lot of stereotypes, and biased information

that get into the database of the GenAI machines that

impact the generated outcome.” (P18)

As a result, many participants reported being distrustful of the output, needing to validate the produced outcomes, and proposed to treat GenAI’s output more as a "suggestion" (P12) or a "second opinion" (P11), that can be wrong just like a human. Due to the errors, one participant demonstrated frustration and questioned the use of GenAI: "what is the point if I have to validate the AI tool’s outcome again?" (P14).

4.3.2 Over reliance on GenAI. Our participants highlighted con- cerns about individuals potentially becoming overly reliant on GenAI. The potential consequences of excessive reliance on gener- ative AI applications that were mentioned by participants included inefficiency, reduced autonomy, and a potential disconnect from in- dividual problem-solving capabilities. Some participants explained: “People trying to use AI for everything that it is not

needed, and they spend more time on the right prompt

instead of doing it on their own." (P23)

Another participant expressed their concern with over-reliance on AI which can potentially lead to a reduction in individuals’ autonomy and self-reliance:

“If people are over reliant on AI tools, as an educator,

my concern is that they can’t think for themselves.”

(P19)

Two senior UX researchers expressed their concerns about the potential consequences of junior researchers, who may not have extensive experience in their field, relying too heavily on GenAI:

“I worry about junior researchers, who don’t have a

lot of experience, over-relying on AI models because

I know what a bad piece of data looks like and I know

what bad research design looks like [but they might

not].” (P6)

“I’ve seen people use [GenAI] because they just want

to get away with not doing mundane work. For ex-

ample, we have a system where researchers share

insights [by writing online] posts. I had one [junior

employee] who started writing the posts in ChatGPT,

and I immediately noticed this because the text was so

boring. And I told them, no, you cannot do this, you

have to write yourself, make it succinct and interest-

ing. It’s like this doesn’t accomplish the task, people

are gonna tune out when they see this AI generated

content. It’s not interesting.” (P7)

4.3.3 Need for GenAI training. Participants indicated needs and interests to learn more about the capabilities of current GenAI tools, improving their abilities two write prompts and interact with AI, as well as improving their skills to assess GenAI output. One participant wondered if "thinking and putting time to make the prompt" (P16) was worth the effort, and another was convinced that people "spend more time on the right prompt instead of doing it on their own" (P23). Some participants specifically highlighted the need for training:

"Giving prompts is hard and time-consuming. [...]

People have to learn how and where to use [GenAI]

and then use it in a correct way." (P5)

"I think I use only 5% of the capability of ChatGPT,

and it’s so helpful for me. I’d love to explore more. [...]

I just need some courses to understand the underlying

technology a little bit better because I think that would

help me learn more about its limitations, and then

also help me approach the output a little bit more

critically." (P6)

Another participant elaborated that not being properly trained on GenAI might contain risks with regards to confidentiality:

"It’s important to understand how to utilize AI with

customers’ data without going over the border with

intellectual property issues." (P2)

4.3.4 Improvement of GenAI for design-focused activities. Our par- ticipants highlighted shortcomings in current GenAI tools espe- cially with regards to design-focused tasks, highlighting that GenAI tools need to be more "user-centered" (P24), consider the "designer’s perspective" (P2), and generate more "meaningful" output (P1). Par- ticipants requested features like tying GenAI output to provided design systems (P2), and having AI provide suggestions during UI design (P5).

Participants also mentioned that most GenAI tools do not keep records of their previous interactions and data, resulting in users having to "repeat everything." (P5) becase GenAI does not "keep conversations in the context", and prevents users from building"complex projects" with GenAI (P13). One participant explained:

“I need previous research knowledge in the data anal-

ysis which the AI doesn’t have. I need the capability

to have the record and insights from the [previously

used] data and its analysis to involve them [in my

current analysis].” (P17)

Our diverse participants also highlighted issues regarding lan- guage and cultural nuances. One participant highlighted that GenAI "only works well in English and not in the language that I need to write my contents" (P11), and another noted that GenAI "doesn’t know the audience and the proper tone based on the background and the cultures of the audiences from various countries" (P20).

### 5 DISCUSSION

In this section, we first summarize our results in relation to our research questions, and discuss the implications from our results and draw connections to prior research (subsections 5.1–5.3). Then, we provide recommendations targeting companies, UX practition- ers, and GenAI developers (subsection 5.4). Finally, we discuss the limitations in our work and provide directions for future research (subsection 5.5).

### 5.1 RQ1: How Are Companies Allowing GenAI

### Use in Their UX Departments and What Policies Are in Place?

According to our results, UX practitioners were largely free to ex- periment with and use GenAI to their liking. However, the majority of our participants reported a considerable lack of formal policies, initiatives, and communication from their employer in regard to GenAI use. Among them, some participants reported that they were informally told to be "cautious" or "careful", while some reported that this was simply "expected". However, some participants re- ported that GenAI tools had been blocked in company computers, but even so many of them had not received further guidance. These participants reported taking some maneuvers around the policies, by using GenAI in their personal computers for work that did not involve sensitive data. In a few occasions, participants reported that their company had licensed a private instance of a GenAI tool, or even developed their own tools; in both cases, this allowed them to safely feed company and customer data into the GenAI tools.

Regardless of their employers’ views or (lack of) initiatives re- garding GenAI use, participants frequently highlighted their in- dividual professionalism and sense of responsibility when using GenAI. Despite the lack of policies or communication from the company, participants stressed that they would not insert sensitive company information into external GenAI tools. While this level of professionalism among UX practitioners is positive and respectable, we argue that the lack of responsibility and initiatives demonstrated by companies in this regard is concerning. It is worth wondering how this might tie into legal issues and the treatment of individ- ual employees if, for example, an employee accidentally shared

sensitive information via an external GenAI tool. In other areas of research, the need for new policies is already widely recognized [20, 34]. Furthermore, other large institutions like universities, have already widely adopted GenAI policies that cover multiple stake- holders like staff, faculty, and students [49 ]. It is surprising, then, that we witnessed such a strong lack of policies, and not only that, but also a lack of communication about GenAI in general.

Participants highlighted that the reasons for some of their em- ployers blocking GenAI tools, or encouraging caution, were largely related to matters of data privacy, confidentiality, and intellectual property. It is likely that large corporations storing vast amounts of sensitive data, and companies in particularly vulnerable indus- tries like banking and financing, are having an especially tough time navigating the recent rise of GenAI. Even though not many of our participants were employed in small companies, they gener- ally seemed to more readily embrace the possibilities that GenAI offered. It should be acknowledged that the companies’ concerns are valid. GenAI tools like ChatGPT are vulnerable in many ways; they can be attacked, and they can be used maliciously [28]. At the same time, cybercriminals now have more advanced tools, some AI-enhanced, for launching cyber attaks [28].

### 5.2 RQ2: How are UX Practitioners and UX

### Teams integrating GenAI into their Work Practices?

In regards to our RQ2, we identified a significant lack of team prac- tices and discussions regarding GenAI. Most participants reported that they made decisions about GenAI use independently of oth- ers and that they did not discuss it with their team members or managers. Some even reported that they did not share content with others that they produced with GenAI. Wider adoption of tools (e.g., tools shared or used within the entire UX team) was rare.

We believe this finding is extremely surprising and in some ways concerning. UX and HCI theory and practices have been evolving for decades, and significant evolutions have often been triggered by technological developments [41]. Moreover, UX fields are inherently collaborative where UX practitioners often work closely together [11, 12, 40], and existing research has widely recognized the value of collaboration [70] and co-design [65] in UX.

We are left wondering, then, what might explain this surprising lack of team practices and discussions regarding GenAI. Based on our other findings and prior research, we can speculate on the role of two possible factors. One possible explanation is that UX practitioners might feel uncertain or cautious about how GenAI is perceived by their colleagues and superiors, or feel cautious about being too open about GenAI use so that their employer will not take action against it or see the employee in a bad light. Some of our participants’ responses seemed to hint at an almost strategic silence about GenAI. This uncertainty may also link to the lack of company policies and communication, and employees may have been unsure about how their employer feels about GenAI.

Another possible explanation is that we might be witnessing a transformation of the UX fields where AI is partly replacing human collaborators. There is a wealth of research demonstrating effective human-AI collaboration in many UX activities like creation and ideation [13 , 36 , 56 , 67 ], drawing and sketching [16, 35, 55], and data analysis [38, 39 ]. Fan et al. [23], for example, demonstrated that some UX evaluators in their study felt like they were working with a "junior colleague" when working with an AI.

Aside from the lack of team practices, UX practitioners reported what they used GenAI for and how they perceived its effects. Gen- erally, there was widespread recognition among UX practitioners that GenAI can make their practices more efficient. This is in line with earlier findings about ML and AI in general [7, 48, 75 ] as well as GenAI specifically [43, 67].

UX researchers in particular found GenAI useful for their prac- tices and are utilizing GenAI tools at multiple stages of their work. Common practices for practitioners conducting UX research with GenAI included generating drafts for a research plan, summarizing existing research and results, and conducting data analysis, and the UX practitioners saw value in using GenAI for these tasks. This partly contradicts earlier results: Lu et al. [48] reported almost op- posite results in that their participants mainly used AI system to work on graphical interface elements but did not find them helpful for activities such as user interviews and user testings. However, Lu et al. [48], conducted their study before the recent GenAI wave; we believe that this demonstrates the power of the new GenAI tools and how they can transform and assists with UX research.

For design work, GenAI use seemed to largely focus on the early stages of design, like brainstorming and creating initial visualiza- tions for communicating ideas. It is not surprising that GenAI was found useful for these activities: prior research supports this and has also proposed AI-enhanced brainstorming and creativity tools and verified their effectiveness [e.g., 13, 32, 67].

Beyond these activities, our interviewees largely perceived GenAI to be lacking for additional design-focused tasks like wireframing, graphic design, and prototyping, highlighting many shortcomings in the current tools. This finding is interesting because existing re- search has proposed and evaluated a plethora of AI-enhanced tools for design activities with good results, like graphic design [27, 90], wireframing [10 , 24], layout optimization [17, 68], and prototyping [50]. Perhaps, then, part of the problem is that such tools are not widely available to UX practitioners, or the practitioners are not aware of them or do not know how to use them. This may link to some earlier findings about UX practitioners being unaware of the possibilities of AI [1]; it is interesting that this might still be the case despite GenAI raising people’s awareness so thoroughly. Still, it is clear that despite all these challenges and shortcomings, UX designers still find value in GenAI especially in the early stages of their work, albeit hoping for advancements in the future.

### 5.3 RQ3: What are the Current Challenges and

### Needs Regarding the Integration of GenAI into UX Industry Practices?

Participants reported various challenges they faced with GenAI and, in the same vein, requested multiple features and improvements for GenAI that would help them in their UX practices.

Most commonly, participants reported that GenAI can produce inaccurate content, resulting in the content having to be checked. As a result, many stated that rather than trusting the GenAI tools completely, they treated them more as a second opinion, that can occasionally be wrong and must sometimes be corrected or ignored.

This in part highlights that UX practitioners must build their own fundamental base skills to be able to assess GenAI outputs. At the same time, we argue that even when GenAI eventually improves and produces more accurate content, people should continue to be in control and not let AI take over; after all, the fundamental objective of AI is to improve human capabilities, not replace them [81]. Concerns about AI "taking over" have been voiced by employ- ees in various fields, also in UX, both in our study as well as prior research [43].

Second, participants reported concerns about others relying on GenAI too much. The reported consequences included reduced efficiency, hurting the UX practitioner’s ability for critical think- ing, and being unable to identify low-quality output due to not having sufficiently developed their own skills. This concern was prominent among senior UX practitioners, who expressed concern over junior employee’s over-dependence on GenAI, and some had already witnessed such cases. This is an interesting finding because in contrast, another study found that junior designers themselves were concerned about skill degradation and job impact [43].

Third, participants expressed a desire to receive more training on GenAI. Many participants pointed to learning to write "better prompts" for GenAI, which they said often required iteration and trial and error before they got the outcome they wanted. Prior research has also found that articulating instructions to the sys- tem are a significant part of GenAI-human interaction [67 ], and especially users with no AI expertise can struggle with generating prompts [88]. In the same vein, participants wished to better un- derstand how AI and tools worked "under the hood" and how they produced their output, believing it would help them use it more efficiently and comprehensively. Indeed, prior research has found that uncertainty surrounding AI’s capabilities can be a challenge for designers [19, 85]. Other research has also provided evidence that providing output explanations can improve the user’s perceived understanding of the AI [23]. Li et al. [43] also found that UX prac- titioners wished for improved AI literacy among both senior and junior designers.

Our participants reported several expected benefits from train- ing, like increased efficiency (due to reduced time spent writing and iterating prompts), increased ability to assess output quality, reduced chance of misuse of customer data and other sensitive data, and increased resilience to AI "taking over" the work.

Finally, participants reported things they wish GenAI tools would focus on or functions they would provide. The participants gen- erally called for more focus on UX and UI design, stating that the current tools were not mature enough for adoption. In a similar vein, participants expressed that GenAI tools should be more "human- centric", that is, keep the user’s needs in mind that GenAI was being used to design for. Prior research recognizes the need to keep AI assistants designer-centric [18 ], so it could be argued that one challenge for AI assistants is to consider both the designer’s needs and the end user’s needs. Other, specific requests included better management of previous work with GenAI, allowing users to refer to earlier conversations and analyses, factoring in the provided design system when generating UIs, predicting the designer’s in- tentions and providing suggestions, more comprehensive language and translation support, and better tools for designing icons.

### 5.4 Recommendations for Companies, Teams,

### UX Practitioners, and GenAI Developers

5.4.1 Recommendation #1: Companies need to set up formal policies, communicate with employees, and take responsibility for GenAI use. We urge companies to set up formal policies and practices regarding GenAI use to the benefit of not only the company but also their employees. Our results suggest that companies are relying on the employees’ professionalism and goodwill (e.g., to not abuse com- pany data). This opens up potential legal issues for the company but also unfairly shifts the responsibility to individual employees. It is undoubtedly complex for companies to navigate GenAI tools in regard to data privacy and confidentiality, especially for large corporations and those in particularly sensitive sectors like finance. However, while these policies are being developed, compa- nies should already actively engage in discussions and communi- cation with their UX practitioners, offer updates, and ensure the overall transparency of the process. Lack of communication is likely to foster uncertainty among workers, which is highlighted with AI because it links to fears about job stability and AI replacing human workers [76], even among UX practitioners [43].

Some resources and guidance exist that companies can leverage to develop their own policies. Some universities have begun to set up their own GenAI policies [49]. Researchers have also drafted initial policy considerations for policy makers [47 ], which touch on many important topics like copyright considerations, AI biases, and potential misuse.

5.4.2 Recommendation #2: Companies should offer GenAI training to UX practitioners. Training was explicitly requested by many par- ticipants. In addition, our participants reported several challenges and concerns regarding GenAI use that could be solved or alleviated with training. Based on our findings, company-provided training could focus on the following aspects:

• Writing GenAI prompts. Our participants commonly re- ported spending much time writing and iterating on prompts, some so much so that they questioned whether GenAI was actually worth the time investment. Existing research pro- vides various strategies for improving prompts, such as giv- ing examples of desired outcomes, writing more "code-like"prompts, and including repetition in prompts [88], which could be utilized in training UX practitioners.

• Fundamental skills and assessment of GenAI output. Participants reported concerns over some UX practitioners, especially junior employees, relying too much on GenAI without a sufficient ability to assess the quality of the output. Prior research has also identified concerns among UX prac- titioners about skill degradation [43]. Therefore, training could focus on developing their ability to assess the output quality, but also junior employees’ fundamental UX skills.

• Understanding of AI. Some participants expressed that they did not really understand AI in general and how specific GenAI tools work, and what their capabilities are, believing that it hindered their ability to use GenAI effectively. Espe- cially, participants highlighted that they could understand and assess GenAI’s output better if they understood how the AI came to that conclusion. Guidelines and resources

exist [e.g., 4, 58] that are intended to help designers when designing AI-enhanced systems; however, existing research notes that such resources can also help people learn about AI, as well as help develop internal resources [87].

• Awareness of GenAI tools. While practically all intervie- wees used GenAI on some level in their work, some practi- tioners used it for more surface-level and early work. Espe- cially UX and UI designers expressed that they did not think GenAI tools were mature enough to be effective in more involved areas of their work, like wireframing and graphic design. Yet, as already discussed, existing research proposes various tools and method for such activities. At the same time, many design platforms are already offering built-in GenAI features as well as plugins. Therefore, training could focus on raising awareness of various kinds of AI tools tai- lored for designers that UX practitioners might not be aware of, such as tools for wireframing [10, 24] and graphic design [90], and further train on their use and capabilities.

5.4.3 Recommendation #3: UX teams should discuss, share, and build GenAI-enhanced UX processes and foster collaboration. We urge UX practitioners and their managers to engage in discussions with their team members, to share knowledge and ideas about GenAI and begin building GenAI-enhanced UX practices and processes. Collab- orative approaches would ensure alignment with new methodolo- gies and technologies, and encourage innovation and transparency. Sharing knowledge and experiences about GenAI tools can help in identifying best practices, troubleshooting common issues, and exploring new ways to apply these tools.

Shared GenAI practices would undoubtedly make the use of these tools more efficient and productive, as well as foster learning and help UX practitioners with some of the challenges they currently face with GenAI. Some recent work can provide valuable guidance here; Han et al. [29] discuss how individuals can work together to write effective GenAI prompts, and learn from each other in the process. Similarly, shared practices and active discussions and mentoring can play a key role in onboarding and training junior employees and interns. While junior UX practitioners certainly have an individual responsibility to develop their skills and use GenAI responsibly, senior practitioners and managers also have a responsibility towards their junior colleagues.

5.4.4 Recommendation #4: GenAI tools should provide better sup- port to UX designers. Our participants frequently reported that they wished GenAI tools supported their design work better. Participants called for better support for activities like wireframing, graphic de- sign, and prototyping. As already discussed, plenty of AI-enhanced tools for these purposes have been built, but they may exist mainly as research prototypes or may not otherwise be widely available. Therefore, we identify an opportunity to integrate these tools into the more widely used GenAI tools. More broadly, we identify an opportunity for GenAI tools to offer multiple functionalities and modes, which would also support collaboration and practices in UX teams, by enabling team-wide use of the same tools. In another study, participants made a similar suggestion to combine text and image generation capabilities into one interface [67].

5.4.5 Recommendation #5: GenAI tools should support the principles of explainable AI. The practitioners in our study, and other prior research, noted that they are occasionally distrustful of AI tools and their output. While is it strongly recommended that GenAI users indeed do not blindly trust the output and should be capable of assessing its quality, this lead to further issues like hesitancy to utilize seemingly high-quality output due to not knowing how the AI came to that suggestion. Similarly, participants often reported that they wished to have a better understanding of the AI’s thought process. These matters link to principles of explainable AI (XAI), such as transparency and accountability [8, 78, 80]. A quick analysis at the currently popular GenAI tools like ChatGPT, DALL-E, and Midjourney reveals that they do not fully support these principles. Therefore, we recommend that the developers of GenAI engage more with explainable AI to support transparency and the users’ ability to critically assess the AI’s output.

### 5.5 Limitations and Future Work

Because we are dealing with the rapidly changing landscapes of GenAI and UX, we acknowledge that some of our results are rather a snapshot of the current status in the UX industry. While it is not clear how long some of our results will hold, this opens up opportunities for future research. We also emphasize, as outlined in our discussion and recommendations, that we want things to change, and we view our paper as a call-to-action for UX practi- tioners, teams, and companies. Therefore, it would be valuable to explore UX industry practices in the near future to monitor how these practices are evolving and to identify opportunities for HCI researchers to contribute to building and evaluating these practices. Furthermore, we chose interviews as an appropriate method because we focused on acquiring qualitative insights into the UX professionals’ practices as well as team and company culture. We believe that our results are strong especially because participants also provided information about their colleagues and companies, broadening our results. That said, given the method, we cannot claim generalizability beyond our sample. Rather, now that we have identified critical needs regarding GenAI use in UX, such as lack of company policies and team practices, a broader investigation into these matters using other methods (e.g., with an online survey) is warranted. This would also allow for an investigation into how UX practices differ between countries and cultures.

### 6 CONCLUSION

In this work, we investigated industry practices regarding GenAI use in the field of user experience, covering UX design and UX research and similar areas, at three levels: practices among individ- ual UX practitioners, practices and discussions in UX teams, and practices and policies in companies with UX departments.

As some of the most significant and surprising results, we identi- fied a significant lack of policies, practices, and discussions regard- ing GenAI use at both the company level and team level. Instead, individual UX practitioners typically made independent decisions to use GenAI tools in their work, and also showed vigilance for data privacy and confidentiality.

Therefore, we urge companies to adopt GenAI policies and ac- tively communicate with employees as well as offer GenAI-related

training. We also urge UX teams and managers to begin developing GenAI-enhanced practices that foster collaboration in the team. We foresee several benefits from adopting such practices, like increased efficiency, shared responsibility over GenAI use, and lower risk for breaches in data privacy, confidentiality, and intellectual property. Moreover, we highlight how UX researchers in particular have found GenAI useful for their practices and are utilizing GenAI tools at multiple stages of their work, such as writing and creating drafts, designing studies, and analysing data. UX and UI designers, however, typically use GenAI in the early stages for brainstorming and visualization, but find current GenAI tools lacking for advanced design work such as wireframing, graphic design, and prototyping.

### ACKNOWLEDGMENTS

This research was funded, in part, by the Social Sciences and Hu- manities Research Council of Canada (SSHRC Insight Development Grant 430-2022-00577). We thank our interview participants for their time and feedback.

### REFERENCES

[1] Abdallah M. H. Abbas, Khairil Imran Ghauth, and Choo-Yee Ting. 2022. User

[Experience Design Using Machine Learning: A Systematic Review.](https://doi.org/10.1109/ACCESS.2022.3173289) IEEE Access

10 (2022), 51501–51514. [https://doi.org/10.1109/ACCESS.2022.3173289](https://doi.org/10.1109/ACCESS.2022.3173289)

[2] Ahmed Al-sa’di and Dave Miller. 2023. Exploring the Impact of Artificial Intel- ligence language model ChatGPT on the User Experience. International Jour-

[nal of Technology, Innovation and Management (IJTIM)](https://doi.org/10.54489/ijtim.v3i1.195) 3, 1 (May 2023), 1–8. [https://doi.org/10.54489/ijtim.v3i1.195](https://doi.org/10.54489/ijtim.v3i1.195)

[3] James T. Allison, Michel-Alexandre Cardin, Chris McComb, Max Yi Ren, Daniel

Selva, Conrad Tucker, Paul Witherell, and Yaoyao Fiona Zhao. 2022. Special Issue: Artificial Intelligence and Engineering Design. Journal of mechanical design (1990) 144,2(2022).

[4] Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, Adam Fourney, Besmira

Nushi, Penny Collisson, Jina Suh, Shamsi Iqbal, Paul N. Bennett, Kori Inkpen, Jaime Teevan, Ruth Kikin-Gil, and Eric Horvitz. 2019. Guidelines for Human- AI Interaction. In Proceedings of the 2019 CHI Conference on Human Factors in

Computing Systems (Glasgow, Scotland Uk) (CHI ’19). Association for Computing

Machinery, New York, NY, USA, 1–13. [https://doi.org/10.1145/3290605.3300233](https://doi.org/10.1145/3290605.3300233)

[5] J. An, H. Kwak, S. Jung, J. Salminen, M. Admad, and B. Jansen. 2018. Imaginary

People Representing Real Numbers: Generating Personas from Online Social

Media Data. ACM Trans. Web 12, 4, Article 27 (nov 2018), 26 pages. [https: //doi.org/10.1145/3265986](https://doi.org/10.1145/3265986)

[6] Batuhan Asiroglu, Busta Rumeysa Mete, Eyyup Yildiz, Yagiz Nalcakan, Alper

Sezen, Mustafa Dagtekin, and Tolga Ensari. 2019. Automatic HTML Code Genera- tion from Mock-Up Images Using Machine Learning Techniques. In 2019 Scientific

Meeting on Electrical-Electronics & Biomedical Engineering and Computer Science

(EBBT). IEEE, 1–4.

[7] Maxim Bakaev, Sebastian Heil, Vladimir Khvorostov, and Martin Gaedke. 2023. How Many Data Does Machine Learning in Human–Computer Interaction Need?: Re-Estimating the Dataset Size for Convolutional Neural Network-Based Models

of Visual Perception. IT Professional 25, 2 (2023), 23–29. [https://doi.org/10.1109/ MITP.2023.3262923](https://doi.org/10.1109/MITP.2023.3262923)

[8] Nagadivya Balasubramaniam, Marjo Kauppinen, Kari Hiekkanen, and Sari Kujala. 2022. Transparency and Explainability of AI Systems: Ethical Guidelines in

Practice. In Requirements Engineering: Foundation for Software Quality, Vincenzo

Gervasi and Andreas Vogelsang (Eds.). Springer International Publishing, Cham, 3–18.

[9] Sam Bourgault and Jane E. 2023. Exploring the Horizon of Computation for

Creativity. XRDS 29, 4 (jun 2023), 6–9. [https://doi.org/10.1145/3596921](https://doi.org/10.1145/3596921)

[10] Daniel Buschek, Charlotte Anlauff, and Florian Lachner. 2020. Paper2Wire: a case study of user-centred development of machine learning tools for UX

designers. In Proceedings of Mensch Und Computer 2020 (Magdeburg, Germany) [(MuC ’20)](https://doi.org/10.1145/3404983.3405506). Association for Computing Machinery, New York, NY, USA, 33–41. [https://doi.org/10.1145/3404983.3405506](https://doi.org/10.1145/3404983.3405506)

[11] James Cabrera. 2017. Modular design frameworks: A projects-based guide for UI/UX designers. Springer.

[12] Marivi Carlton. 2019. Design + UX Research: The case for collaboration and

separation. (2019). [https://doi.org/@marivi.carlton/design-ux-research-the- case-for-collaboration-and-separation-491ad2164ecb](https://doi.org/@marivi.carlton/design-ux-research-the-case-for-collaboration-and-separation-491ad2164ecb)

[13] Li-Yuan Chiou, Peng-Kai Hung, Rung-Huei Liang, and Chun-Teng Wang. 2023. Designing with AI: An Exploration of Co-Ideation with Image Generators. In

Proceedings of the 2023 ACM Designing Interactive Systems Conference (Pittsburgh,	in Computing Systems (Yokohama, Japan) (CHI ’21)[. Association for Computing](https://doi.org/10.1145/3411764.3445117) PA, USA) [(DIS ’23). Association for Computing Machinery, New York, NY, USA,](https://doi.org/10.1145/3563657.3596001)	Machinery, New York, NY, USA, Article 577, 17 pages. [https://doi.org/10.1145/](https://doi.org/10.1145/3411764.3445117)

1941–1954. [https://doi.org/10.1145/3563657.3596001](https://doi.org/10.1145/3563657.3596001)	[3411764.3445117](https://doi.org/10.1145/3411764.3445117)

[14] Michael Chromik, Florian Lachner, and Andreas Butz. 2020. ML for UX? - An [28] Maanak Gupta, Charankumar Akiri, Kshitiz Aryal, Eli Parker, and Lopamu- Inventory and Predictions on the Use of Machine Learning Techniques for UX	dra Praharaj. 2023. From ChatGPT to ThreatGPT: Impact of Generative AI

Research. In Proceedings of the 11th Nordic Conference on Human-Computer In-	in Cybersecurity and Privacy. IEEE Access 11 (2023), 80218–80245. [https:](https://doi.org/10.1109/ACCESS.2023.3300381) teraction: Shaping Experiences, Shaping Society (Tallinn, Estonia) (NordiCHI ’20).	[//doi.org/10.1109/ACCESS.2023.3300381](https://doi.org/10.1109/ACCESS.2023.3300381)

Association for Computing Machinery, New York, NY, USA, Article 57, 11 pages. [29] Yuanning Han, Ziyi Qiu, Jiale Cheng, and RAY LC. 2024. When Teams Embrace AI: [https://doi.org/10.1145/3419249.3420163](https://doi.org/10.1145/3419249.3420163)	Human Collaboration Strategies in Generative Prompting in a Creative Design

[15] Harsh Dave, Sarah Sonje, Jaswantsingh Pardeshi, Sheetal Chaudhari, and Pooja	Task. In Proceedings of the 2024 CHI Conference on Human Factors in Computing

Raundale. 2021. A survey on Artificial Intelligence based techniques to convert	Systems (Honolulu, HI, USA) (CHI ’24). Association for Computing Machinery, User Interface design mock-ups to code. In 2021 International Conference on	New York, NY, USA, 14 pages. [https://doi.org/10.1145/3613904.3642133](https://doi.org/10.1145/3613904.3642133)

Artificial Intelligence and Smart Systems (ICAIS). IEEE, 28–33.	[30] Rex Hartson and Pardha S Pyla. 2018. The UX book: Agile UX design for a quality [16] Nicholas Davis, Chih-Pin Hsiao, Kunwar Yashraj Singh, and Brian Magerko. 2021.	user experience. Morgan Kaufmann.

Co-Creative Drawing Agent with Object Recognition. Proceedings of the AAAI [31] Lars Erik Holmquist. 2017. Intelligence on Tap: Artificial Intelligence as a New

Conference on Artificial Intelligence and Interactive Digital Entertainment 12,1	Design Material. Interactions 24, 4 (jun 2017), 28–33. [https://doi.org/10.1145/](https://doi.org/10.1145/3085571) (Jun. 2021), 9–15. [https://doi.org/10.1609/aiide.v12i1.12863](https://doi.org/10.1609/aiide.v12i1.12863)	[3085571](https://doi.org/10.1145/3085571)

[17] Niraj Ramesh Dayama, Kashyap Todi, Taru Saarelainen, and Antti Oulasvirta. [32] Angel Hsing-Chi Hwang. 2022. Too Late to be Creative? AI-Empowered Tools in

2020. GRIDS: Interactive Layout Design with Integer Programming. In Proceedings	Creative Processes. In Extended Abstracts of the 2022 CHI Conference on Human of the 2020 CHI Conference on Human Factors in Computing Systems (Honolulu,	Factors in Computing Systems (New Orleans, LA, USA) (CHI EA ’22). Association

HI, USA) (CHI ’20). Association for Computing Machinery, New York, NY, USA,	for Computing Machinery, New York, NY, USA, Article 38, 9 pages. [https:](https://doi.org/10.1145/3491101.3503549) 1–13. [https://doi.org/10.1145/3313831.3376553](https://doi.org/10.1145/3313831.3376553)	[//doi.org/10.1145/3491101.3503549](https://doi.org/10.1145/3491101.3503549)

[18] Sebastiaan De Peuter, Antti Oulasvirta, and Samuel Kaski. 2023. Toward AI [33] Bernard J. Jansen, Joni Salminen, Soon-gyo Jung, and Kathleen Guan. 2021. Eval- assistants that let designers design. AI Mag. 44, 1 (apr 2023), 85–96. [https:](https://doi.org/10.1002/aaai.12077)	uating Data-Driven Personas. Springer International Publishing, Cham, 209–237. [//doi.org/10.1002/aaai.12077](https://doi.org/10.1002/aaai.12077)	[https://doi.org/10.1007/978-3-031-02231-9\_9](https://doi.org/10.1007/978-3-031-02231-9_9)

[19] Graham Dove, Kim Halskov, Jodi Forlizzi, and John Zimmerman. 2017. UX Design [34] Dominik K. Kanbach, Louisa Heiduk, Georg Blueher, Maximilian Schreiter, and

Innovation: Challenges for Working with Machine Learning as a Design Material.	Alexander Lahmann. 2023. The GenAI is out of the bottle: generative artificial

In Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems	[intelligence from a business model innovation perspective.](https://doi.org/10.1007/s11846-023-00696-z) Review of Managerial

(Denver, Colorado, USA) [(CHI ’17). Association for Computing Machinery, New](https://doi.org/10.1145/3025453.3025739)	Science (2023), 1–32. [https://doi.org/10.1007/s11846-023-00696-z](https://doi.org/10.1007/s11846-023-00696-z)

York, NY, USA, 278–288. [https://doi.org/10.1145/3025453.3025739](https://doi.org/10.1145/3025453.3025739)	[35] Pegah Karimi, Jeba Rezwana, Safat Siddiqui, Mary Lou Maher, and Nasrin Dehbo- [20] Yogesh K. Dwivedi, Nir Kshetri, Laurie Hughes, Emma Louise Slade, Anand	zorgi. 2020. Creative sketching partner: an analysis of human-AI co-creativity. Jeyaraj, Arpan Kumar Kar, Abdullah M. Baabdullah, Alex Koohang, Vishnupriya	In Proceedings of the 25th International Conference on Intelligent User Interfaces

Raghavan, Manju Ahuja, Hanaa Albanna, Mousa Ahmad Albashrawi, Adil S. Al-	(Cagliari, Italy) [(IUI ’20). Association for Computing Machinery, New York, NY,](https://doi.org/10.1145/3377325.3377522) Busaidi, Janarthanan Balakrishnan, Yves Barlette, Sriparna Basu, Indranil Bose,	USA, 221–230. [https://doi.org/10.1145/3377325.3377522](https://doi.org/10.1145/3377325.3377522)

Laurence Brooks, Dimitrios Buhalis, Lemuria Carter, Soumyadeb Chowdhury, [36] Jingoog Kim and Mary Lou Maher. 2023. The effect of AI-based inspiration Tom Crick, Scott W. Cunningham, Gareth H. Davies, Robert M. Davison, Rahul Dé,	on human design ideation. [International Journal of Design Creativity and In-](https://doi.org/10.1080/21650349.2023.2167124) Denis Dennehy, Yanqing Duan, Rameshwar Dubey, Rohita Dwivedi, John S. Ed-	novation [11, 2 (2023), 81–98.](https://arxiv.org/abs/https://doi.org/10.1080/21650349.2023.2167124) [https://doi.org/10.1080/21650349.2023.2167124](https://doi.org/10.1080/21650349.2023.2167124) wards, Carlos Flavián, Robin Gauld, Varun Grover, Mei-Chih Hu, Marijn Janssen,	[arXiv:https://doi.org/10.1080/21650349.2023.2167124](https://arxiv.org/abs/https://doi.org/10.1080/21650349.2023.2167124)

Paul Jones, Iris Junglas, Sangeeta Khorana, Sascha Kraus, Kai R. Larsen, Paul [37] [Nir Kshetri. 2023. ChatGPT in Developing Economies.](https://doi.org/10.1109/MITP.2023.3254639) IT Professional 25,2(2023),

| Latreille, Sven Laumer, F. Tegwen Malik, Abbas Mardani, Marcello Mariani, Sunil | 16–19. [https://doi.org/10.1109/MITP.2023.3254639](https://doi.org/10.1109/MITP.2023.3254639) |
| --- | --- |
| Mithas, Emmanuel Mogaji, Jeretta Horn Nord, Siobhan O’Connor, Fevzi Okumus, | [38] Emily Kuang. 2023. Crafting Human-AI Collaborative Analysis for User Ex- |
| Margherita Pagani, Neeraj Pandey, Savvas Papagiannidis, Ilias O. Pappas, Nishith | perience Evaluation. In Extended Abstracts of the 2023 CHI Conference on Hu- |

Pathak, Jan Pries-Heje, Ramakrishnan Raman, Nripendra P. Rana, Sven-Volker	man Factors in Computing Systems (Hamburg, Germany) (CHI EA ’23). Asso- Rehm, Samuel Ribeiro-Navarrete, Alexander Richter, Frantz Rowe, Suprateek	ciation for Computing Machinery, New York, NY, USA, Article 486, 6 pages. Sarker, Bernd Carsten Stahl, Manoj Kumar Tiwari, Wil van der Aalst, Viswanath	[https://doi.org/10.1145/3544549.3577042](https://doi.org/10.1145/3544549.3577042)

Venkatesh, Giampaolo Viglia, Michael Wade, Paul Walton, Jochen Wirtz, and Ryan [39] Emily Kuang, Ehsan Jahangirzadeh Soure, Mingming Fan, Jian Zhao, and Kristen

Wright. 2023. Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary	Shinohara. 2023. Collaboration with Conversational AI Assistants for UX Evalu- perspectives on opportunities, challenges and implications of generative conver-	ation: Questions and How to Ask them (Voice vs. Text). In Proceedings of the 2023

sational AI for research, practice and policy. International Journal of Information	CHI Conference on Human Factors in Computing Systems (Hamburg, Germany) Management 71(2023),102642. [https://doi.org/10.1016/j.ijinfomgt.2023.102642](https://doi.org/10.1016/j.ijinfomgt.2023.102642)	(CHI ’23). Association for Computing Machinery, New York, NY, USA, Article [21] Judith E. Fan, Monica Dinculescu, and David Ha. 2019. collabdraw: An En-	116, 15 pages. [https://doi.org/10.1145/3544548.3581247](https://doi.org/10.1145/3544548.3581247)

vironment for Collaborative Sketching with an Artificial Agent. In Proceed- [40] Emily Kuang, Xiaofu Jin, and Mingming Fan. 2022. “Merging Results Is No Easy

ings of the 2019 Conference on Creativity and Cognition (San Diego, CA, USA)	Task”: An International Survey Study of Collaborative Data Analysis Practices

(C&C ’19). Association for Computing Machinery, New York, NY, USA, 556–561.	Among UX Practitioners. In Proceedings of the 2022 CHI Conference on Human

[https://doi.org/10.1145/3325480.3326578](https://doi.org/10.1145/3325480.3326578)	Factors in Computing Systems (New Orleans, LA, USA) (CHI ’22). Association [22] Mingming Fan, Ke Wu, Jian Zhao, Yue Li, Winter Wei, and Khai N. Truong.	for Computing Machinery, New York, NY, USA, Article 318, 16 pages. [https:](https://doi.org/10.1145/3491102.3517647) 2020. VisTA: Integrating Machine Intelligence with Visualization to Support the	[//doi.org/10.1145/3491102.3517647](https://doi.org/10.1145/3491102.3517647)

Investigation of Think-Aloud Sessions. [IEEE Transactions on Visualization and](https://doi.org/10.1109/TVCG.2019.2934797) [41] Effie Lai-Chong Law, Virpi Roto, Marc Hassenzahl, Arnold P.O.S. Vermeeren, and

Computer Graphics 26, 1 (2020), 343–352. [https://doi.org/10.1109/TVCG.2019.](https://doi.org/10.1109/TVCG.2019.2934797)	Joke Kort. 2009. Understanding, scoping and defining user experience: a survey

[2934797](https://doi.org/10.1109/TVCG.2019.2934797)	approach. In Proceedings of the SIGCHI Conference on Human Factors in Computing

[23] Mingming Fan, Xianyou Yang, TszTung Yu, Q. Vera Liao, and Jian Zhao. 2022.	Systems (Boston, MA, USA) (CHI ’09). Association for Computing Machinery,

Human-AI Collaboration for UX Evaluation: Effects of Explanation and Synchro-	New York, NY, USA, 719–728. [https://doi.org/10.1145/1518701.1518813](https://doi.org/10.1145/1518701.1518813)

nization. Proceedings of the ACM on human-computer interaction 6, CSCW1 (2022), [42] Jonathan Lazar, Jinjuan Heidi Feng, and Harry Hochheiser. 2017. Research methods

1–32.	in human-computer interaction. Morgan Kaufmann.

[24] Nishit Gajjar, Vinoth Pandian Sermuga Pandian, Sarah Suleri, and Matthias [43] Jie Li, Hancheng Cao, Laura Lin, Youyang Hou, Ruihao Zhu, and Abdallah El Ali. Jarke. 2021. Akin: Generating UI Wireframes From UI Design Patterns Using	2023. User Experience Design Professionals’ Perceptions of Generative Artificial

Deep Learning. In 26th International Conference on Intelligent User Interfaces	Intelligence. arXiv preprint arXiv:2309.15237 (2023).

- Companion (College Station, TX, USA) (IUI ’21 Companion)[. Association for](https://doi.org/10.1145/3397482.3450727) [44] Na Li, Jason Mayes, and Ping Yu. 2021. ML Tools for the Web: A Way for Rapid

Computing Machinery, New York, NY, USA, 40–42. [https://doi.org/10.1145/](https://doi.org/10.1145/3397482.3450727)	[Prototyping and HCI Research](https://doi.org/10.1007/978-3-030-82681-9_10). Springer International Publishing, Cham, 315–343. [3397482.3450727](https://doi.org/10.1145/3397482.3450727)	[https://doi.org/10.1007/978-3-030-82681-9\_10](https://doi.org/10.1007/978-3-030-82681-9_10)

[25] Elisa Giaccardi and Johan Redström. 2020. Technology and More-Than-Human [45] Q.Vera Liao and S. Shyam Sundar. 2022. Designing for Responsible Trust in

Design. [Design Issues 36, 4 (09 2020), 33–44.](https://arxiv.org/abs/https://direct.mit.edu/desi/article-pdf/36/4/33/1857682/desi_a_00612.pdf) [https://doi.org/10.1162/desi\_a\_00612](https://doi.org/10.1162/desi_a_00612)	AI Systems: A Communication Perspective. In Proceedings of the 2022 ACM [arXiv:https://direct.mit.edu/desi/article-pdf/36/4/33/1857682/desi\_a\_00612.pdf](https://arxiv.org/abs/https://direct.mit.edu/desi/article-pdf/36/4/33/1857682/desi_a_00612.pdf)	Conference on Fairness, Accountability, and Transparency (Seoul, Republic of [26] Julian Grigera, Jordan Pascual Espada, and Gustavo Rossi. 2023. AI in User	Korea) (FAccT ’22). Association for Computing Machinery, New York, NY, USA, Interface Design and Evaluation. IT professional 25, 2 (2023), 20–22.	1257–1268. [https://doi.org/10.1145/3531146.3533182](https://doi.org/10.1145/3531146.3533182)

[27] Shunan Guo, Zhuochen Jin, Fuling Sun, Jingwen Li, Zhaorui Li, Yang Shi, and [46] Q. Vera Liao, Daniel Gruen, and Sarah Miller. 2020. Questioning the AI: Informing

Nan Cao. 2021. Vinci: An Intelligent Graphic Design System for Generating	Design Practices for Explainable AI User Experiences. In Proceedings of the 2020

Advertising Posters. In Proceedings of the 2021 CHI Conference on Human Factors	CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA)

[(CHI ’20)](https://doi.org/10.1145/3313831.3376590). Association for Computing Machinery, New York, NY, USA, 1–15. [https://doi.org/10.1145/3313831.3376590](https://doi.org/10.1145/3313831.3376590)

[47] Philippe Lorenz, Karine Perset, and Jamie Berryhill. 2023. Initial policy consid- [erations for generative artificial intelligence. 1 (2023). https://doi.org/https: //doi.org/10.1787/fae2d1e6-en](https://doi.org/https://doi.org/10.1787/fae2d1e6-en)

[48] Yuwen Lu, Chengzhi Zhang, Iris Zhang, and Toby Jia-Jun Li. 2022. Bridg- ing the Gap Between UX Practitioners’ Work Practices and AI-Enabled De- sign Support Tools. In Extended Abstracts of the 2022 CHI Conference on Hu- man Factors in Computing Systems (New Orleans, LA, USA) (CHI EA ’22). As- sociation for Computing Machinery, New York, NY, USA, Article 268, 7 pages. [https://doi.org/10.1145/3491101.3519809](https://doi.org/10.1145/3491101.3519809)

[49] Nora McDonald, Aditya Johri, Areej Ali, and Aayushi Hingle. 2024. Genera- tive Artificial Intelligence in Higher Education: Evidence from an Analysis of

Institutional Policies and Guidelines. arXiv preprint arXiv:2402.01659 (2024).

[50] Kevin Moran, Carlos Bernal-Cardenas, Michael Curcio, Richard Bonett, and

Denys Poshyvanyk. 2020. Machine Learning-Based Prototyping of Graphical

User Interfaces for Mobile Apps. IEEE transactions on software engineering 46,2

(2020), 196–221.

[51] Kevin Moran, Boyang Li, Carlos Bernal-Cárdenas, Dan Jelf, and Denys Poshy- vanyk. 2018. Automated Reporting of GUI Design Violations for Mobile Apps. In 2018 IEEE/ACM 40th International Conference on Software Engineering (ICSE). 165–175. [https://doi.org/10.1145/3180155.3180246](https://doi.org/10.1145/3180155.3180246)

[52] Hendrik Müller, Aaron Sedley, and Elizabeth Ferrall-Nunge. 2014. Survey research

in HCI. Ways of Knowing in HCI (2014), 229–266.

[53] Michael Muller, Lydia B Chilton, Anna Kantosalo, Q. Vera Liao, Mary Lou Maher, Charles Patrick Martin, and Greg Walsh. 2023. GenAICHI 2023: Generative AI

and HCI at CHI 2023. In Extended Abstracts of the 2023 CHI Conference on Human

Factors in Computing Systems (Hamburg, Germany) (CHI EA ’23). Association

for Computing Machinery, New York, NY, USA, Article 350, 7 pages. [https: //doi.org/10.1145/3544549.3573794](https://doi.org/10.1145/3544549.3573794)

[54] Michael Muller, Lydia B Chilton, Anna Kantosalo, Charles Patrick Martin, and

Greg Walsh. 2022. GenAICHI: Generative AI and HCI. In Extended Abstracts of

the 2022 CHI Conference on Human Factors in Computing Systems (New Orleans, LA, USA) (CHI EA ’22)[. Association for Computing Machinery, New York, NY,](https://doi.org/10.1145/3491101.3503719) USA, Article 110, 7 pages. [https://doi.org/10.1145/3491101.3503719](https://doi.org/10.1145/3491101.3503719)

[55] Changhoon Oh, Jungwoo Song, Jinhan Choi, Seonghyeon Kim, Sungwoo Lee, and

Bongwon Suh. 2018. I Lead, You Help but Only with Enough Details: Understand- ing User Experience of Co-Creation with Artificial Intelligence. In Proceedings of

the 2018 CHI Conference on Human Factors in Computing Systems (Montreal QC, Canada) (CHI ’18). Association for Computing Machinery, New York, NY, USA, 1–13. [https://doi.org/10.1145/3173574.3174223](https://doi.org/10.1145/3173574.3174223)

[56] Changhoon Oh, Jungwoo Song, Jinhan Choi, Seonghyeon Kim, Sungwoo Lee, and

Bongwon Suh. 2018. I Lead, You Help but Only with Enough Details: Understand- ing User Experience of Co-Creation with Artificial Intelligence. In Proceedings of

the 2018 CHI Conference on Human Factors in Computing Systems (Montreal QC, Canada) (CHI ’18). Association for Computing Machinery, New York, NY, USA, 1–13. [https://doi.org/10.1145/3173574.3174223](https://doi.org/10.1145/3173574.3174223)

[57] Thomas Olsson and Kaisa Väänänen. 2021. How does AI challenge design

practice? Interactions 28, 4 (jun 2021), 62–64. [https://doi.org/10.1145/3467479](https://doi.org/10.1145/3467479)

[58] Google PAIR. 2021. People + AI Guidebook. [https://pair.withgoogle.com/ guidebook/](https://pair.withgoogle.com/guidebook/)

[59] Desy Intan Permatasari, Fadilah Fahrul Hardiansyah, Mayshella Ainun Wakhi- dah, and Maulidan Bagus Afridian Rasyid. 2021. UX Design Documentation

Application Using The Five Planes Method. In Proceedings of the 6th International

Conference on Sustainable Information Engineering and Technology (Malang, In- donesia) (SIET ’21). Association for Computing Machinery, New York, NY, USA,

29–32. [https://doi.org/10.1145/3479645.3479688](https://doi.org/10.1145/3479645.3479688)

[60] Muhammad Asif Razzaq, Jamil Hussain, Jaehun Bang, Cam-Hao Hua, Fa- had Ahmed Satti, Ubaid Ur Rehman, Hafiz Syed Muhammad Bilal, Seong Tae

Kim, and Sungyoung Lee. 2023. A Hybrid Multimodal Emotion Recognition

[Framework for UX Evaluation Using Generalized Mixture Functions.](https://doi.org/10.3390/s23094373) Sensors 23, 9(2023). [https://doi.org/10.3390/s23094373](https://doi.org/10.3390/s23094373)

[61] Steven P. Reiss, Yun Miao, and Qi Xin. 2018. Seeking the user interface. [Automated](https://doi.org/10.1007/s10515-017-0216-3)

Software Engineering 25, 1 (2018), 157–193. [https://doi.org/10.1007/s10515-017- 0216-3](https://doi.org/10.1007/s10515-017-0216-3)

[62] Joni Salminen, Soon-Gyo Jung, Jisun An, Haewoon Kwak, and Bernard J. Jansen. 2018. Findings of a User Study of Automatically Generated Personas. In Extended

Abstracts of the 2018 CHI Conference on Human Factors in Computing Systems

(Montreal QC, Canada) [(CHI EA ’18). Association for Computing Machinery, New](https://doi.org/10.1145/3170427.3188470)

York, NY, USA, 1–6. [https://doi.org/10.1145/3170427.3188470](https://doi.org/10.1145/3170427.3188470)

[63] Joongi Shin, Michael A. Hedderich, AndréS Lucero, and Antti Oulasvirta. 2022. Chatbots Facilitating Consensus-Building in Asynchronous Co-Design. In Pro-

ceedings of the 35th Annual ACM Symposium on User Interface Software and Tech- nology (Bend, OR, USA) (UIST ’22). Association for Computing Machinery, New York, NY, USA, Article 78, 13 pages. [https://doi.org/10.1145/3526113.3545671](https://doi.org/10.1145/3526113.3545671)

[64] Joon Gi Shin, Janin Koch, Andrés Lucero, Peter Dalsgaard, and Wendy E. Mackay. 2023. Integrating AI in Human-Human Collaborative Ideation. In Extended

Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems

(Hamburg, Germany) (CHI EA ’23)[. Association for Computing Machinery, New](https://doi.org/10.1145/3544549.3573802) York, NY, USA, Article 355, 5 pages. [https://doi.org/10.1145/3544549.3573802](https://doi.org/10.1145/3544549.3573802) [65] Marc Steen. 2013. [Co-Design as a Process of Joint Inquiry and Imagination.](https://doi.org/10.1162/DESI_a_00207) [Design Issues 29, 2 (04 2013), 16–28.](https://arxiv.org/abs/https://direct.mit.edu/desi/article-pdf/29/2/16/1715163/desi_a_00207.pdf) [https://doi.org/10.1162/DESI\_a\_00207](https://doi.org/10.1162/DESI_a_00207) [arXiv:https://direct.mit.edu/desi/article-pdf/29/2/16/1715163/desi\_a\_00207.pdf](https://arxiv.org/abs/https://direct.mit.edu/desi/article-pdf/29/2/16/1715163/desi_a_00207.pdf) [66] Åsne Stige, Efpraxia D. Zamani, Patrick Mikalef, and Yuzhen Zhu. 2023. Artificial intelligence (AI) for user experience (UX) design: a systematic literature review and future research agenda. Information technology & people (West Linn, Or.) (2023).

[67] Jakob Tholander and Martin Jonsson. 2023. Design Ideation with AI - Sketching, Thinking and Talking with Generative Machine Learning Models. In Proceedings of the 2023 ACM Designing Interactive Systems Conference (Pittsburgh, PA, USA) [(DIS ’23)](https://doi.org/10.1145/3563657.3596014). Association for Computing Machinery, New York, NY, USA, 1930–1940. [https://doi.org/10.1145/3563657.3596014](https://doi.org/10.1145/3563657.3596014)

[68] Kashyap Todi, Daryl Weir, and Antti Oulasvirta. 2016. Sketchplore: Sketch and Explore with a Layout Optimiser. In Proceedings of the 2016 ACM Conference on Designing Interactive Systems (Brisbane, QLD, Australia) (DIS ’16). Association for Computing Machinery, New York, NY, USA, 543–555. [https://doi.org/10.1145/ 2901790.2901817](https://doi.org/10.1145/2901790.2901817)

[69] Alex Tyson and Emma Kikuchi. 2021. Growing public concern about the role of artificial intelligence in daily life. (2021). [https://www.pewresearch.org/short- reads/2023/08/28/growing-public-concern-about-the-role-of-artificial- intelligence-in-daily-life/](https://www.pewresearch.org/short-reads/2023/08/28/growing-public-concern-about-the-role-of-artificial-intelligence-in-daily-life/)

[70] Russ Unger and Carolyn Chandler. 2023. A Project Guide to UX Design: For user experience designers in the field or in the making, 3rd Edition. New Riders.

[71] Mojtaba Vaismoradi and Sherrill Snelgrove. 2019. Theme in Qualitative Content Analysis and Thematic Analysis. Forum Qualitative Sozialforschung / Forum: Qualitative Social Research [20, 3 (Sep. 2019). https://doi.org/10.17169/fqs-20.3.3376](https://doi.org/10.17169/fqs-20.3.3376) [72] Mojtaba Vaismoradi, Hannele Turunen, and Terese Bondas. 2013. Content analy- sis and thematic analysis: Implications for conducting a qualitative descriptive study. Nursing & Health Sciences 15, 3 (2013), 398–405. [https://doi.org/10.1111/](https://doi.org/10.1111/nhs.12048) [nhs.12048 arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/nhs.12048](https://arxiv.org/abs/https://onlinelibrary.wiley.com/doi/pdf/10.1111/nhs.12048)

[73] Vera van der Burg, Gijs de Boer, Alkim Almila Akdag Salah, Senthil Chan- drasegaran, and Peter Lloyd. 2023. Objective Portrait: A practice-based in- quiry to explore Al as a reflective design partner. In Proceedings of the 2023 ACM Designing Interactive Systems Conference (Pittsburgh, PA, USA) (DIS ’23). Association for Computing Machinery, New York, NY, USA, 387–400. [https: //doi.org/10.1145/3563657.3595974](https://doi.org/10.1145/3563657.3595974)

[74] Willem Van Der Maden, Evert Van Beek, Iohanna Nicenboim, Vera Van Der Burg, Peter Kun, James Derek Lomas, and Eunsu Kang. 2023. Towards a Design (Re- search) Framework with Generative AI. In Companion Publication of the 2023 ACM Designing Interactive Systems Conference (Pittsburgh, PA, USA) (DIS ’23 [Companion)](https://doi.org/10.1145/3563703.3591453). Association for Computing Machinery, New York, NY, USA, 107–109. [https://doi.org/10.1145/3563703.3591453](https://doi.org/10.1145/3563703.3591453)

[75] Roberto Verganti, Luca Vendraminelli, and Marco Iansiti. 2020. Innovation and Design in the Age of Artificial Intelligence. [Journal of Product Innova-](https://doi.org/10.1111/jpim.12523) [tion Management 37, 3 (2020), 212–227.](https://arxiv.org/abs/https://onlinelibrary.wiley.com/doi/pdf/10.1111/jpim.12523) [https://doi.org/10.1111/jpim.12523](https://doi.org/10.1111/jpim.12523) [arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/jpim.12523](https://arxiv.org/abs/https://onlinelibrary.wiley.com/doi/pdf/10.1111/jpim.12523)

[76] Emmanuelle Walkowiak and Trent MacDonald. 2023. Generative AI and the Workforce: What Are the Risks? Available at SSRN (2023). [https://doi.org/10. 2139/ssrn.4568684](https://doi.org/10.2139/ssrn.4568684)

[77] Dieter P. Wallach, Lukas A. Flohr, and Annika Kaltenhauser. 2020. Beyond the Buzzwords: On the Perspective of AI in UX and Vice Versa. In Artificial Intelligence in HCI, Helmut Degen and Lauren Reinerman-Jones (Eds.). Springer International Publishing, Cham, 146–166.

[78] Danding Wang, Qian Yang, Ashraf Abdul, and Brian Y. Lim. 2019. Design- ing Theory-Driven User-Centric Explainable AI. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (Glasgow, Scotland Uk) (CHI ’19). Association for Computing Machinery, New York, NY, USA, 1–15. [https://doi.org/10.1145/3290605.3300831](https://doi.org/10.1145/3290605.3300831)

[79] Wavestone. 2023. Data and AI Executive Leadership Survey 2024. (2023). [https://www.wavestone.com/en/insight/data-and-ai-executive-leadership- survey-2024/](https://www.wavestone.com/en/insight/data-and-ai-executive-leadership-survey-2024/)

[80] Feiyu Xu, Hans Uszkoreit, Yangzhou Du, Wei Fan, Dongyan Zhao, and Jun Zhu. 2019. Explainable AI: A Brief Survey on History, Research Areas, Approaches and Challenges. In Natural Language Processing and Chinese Computing, Jie Tang, Min-Yen Kan, Dongyan Zhao, Sujian Li, and Hongying Zan (Eds.). Springer International Publishing, Cham, 563–574.

[81] Wei Xu. 2019. Toward Human-Centered AI: A Perspective from Human-Computer Interaction. Interactions 26, 4 (jun 2019), 42–46. [https://doi.org/ 10.1145/3328485](https://doi.org/10.1145/3328485)

[82] Wei Xu. 2023. AI in HCI Design and User Experience. arXiv:2301.00987 [cs.HC] [83] Qian Yang. 2017. The role of design in creating machine-learning-enhanced user experience. In 2017 AAAI spring symposium series.

[84] Qian Yang, Alex Scuito, John Zimmerman, Jodi Forlizzi, and Aaron Steinfeld. 2018. Investigating How Experienced UX Designers Effectively Work with Machine Learning. In Proceedings of the 2018 Designing Interactive Systems Conference

(Hong Kong, China) [(DIS ’18). Association for Computing Machinery, New York,](https://doi.org/10.1145/3196709.3196730) NY, USA, 585–596. [https://doi.org/10.1145/3196709.3196730](https://doi.org/10.1145/3196709.3196730)

[85] Qian Yang, Aaron Steinfeld, Carolyn Rosé, and John Zimmerman. 2020. Re- Examining Whether, Why, and How Human-AI Interaction Is Uniquely Difficult to Design. In Proceedings of the 2020 CHI Conference on Human Factors in Comput- ing Systems (Honolulu, HI, USA) (CHI ’20). Association for Computing Machinery, New York, NY, USA, 1–13. [https://doi.org/10.1145/3313831.3376301](https://doi.org/10.1145/3313831.3376301)

[86] Nur Yildirim, Changhoon Oh, Deniz Sayar, Kayla Brand, Supritha Challa, Violet Turri, Nina Crosby Walton, Anna Elise Wong, Jodi Forlizzi, James McCann, and John Zimmerman. 2023. Creating Design Resources to Scaffold the Ideation of AI Concepts. In Proceedings of the 2023 ACM Designing Interactive Systems Conference (Pittsburgh, PA, USA) (DIS ’23). Association for Computing Machinery, New York, NY, USA, 2326–2346. [https://doi.org/10.1145/3563657.3596058](https://doi.org/10.1145/3563657.3596058)

[87] Nur Yildirim, Mahima Pushkarna, Nitesh Goyal, Martin Wattenberg, and Fer- nanda Viégas. 2023. Investigating How Practitioners Use Human-AI Guidelines: A Case Study on the People + AI Guidebook. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (Hamburg, Germany) (CHI ’23). Association for Computing Machinery, New York, NY, USA, Article 356, 13 pages. [https://doi.org/10.1145/3544548.3580900](https://doi.org/10.1145/3544548.3580900)

[88] J.D. Zamfirescu-Pereira, Richmond Y. Wong, Bjoern Hartmann, and Qian Yang. 2023. Why Johnny Can’t Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (Hamburg, Germany) (CHI ’23). Association for Computing Machinery, New York, NY, USA, Article 437, 21 pages. [https://doi.org/10.1145/ 3544548.3581388](https://doi.org/10.1145/3544548.3581388)

[89] Guanglu Zhang, Ayush Raina, Jonathan Cagan, and Christopher McComb. 2021. A cautionary tale about the impact of AI on human design teams. Design studies 72 (2021), 100990–.

[90] Xinru Zheng, Xiaotian Qiao, Ying Cao, and Rynson Lau. 2019. Content-aware generative modeling of graphic design layouts. ACM transactions on graphics 38, 4 (2019), 1–15.

[91] Oksana N<sub>,</sub> ikiforova, Vitaly Zabiniako, Jurijs Kornienko, Madara Gasparoviča- As¯ıte, and Amanda Silin<sub>,</sub>a. 2021. Mapping of Source and Target Data for Applica- tion to Machine Learning Driven Discovery of IS Usability Problems. [Applied](https://doi.org/doi:10.2478/acss-2021-0003) Computer Systems [26, 1 (2021), 22–30. https://doi.org/doi:10.2478/acss-2021-0003](https://doi.org/doi:10.2478/acss-2021-0003)

### A INTERVIEW QUESTIONS

### A.1 Demographic Questions

• How old are you?

• What gender do you identify with?

• What is your country of residence?

• What is your level of education, and field?

• What is your occupation, including your exact job title?

• What is type of your current employment? Are you working for a company full-time or part-time, do you freelance, or something else?

• How many years of experience do you have as a UX profes- sional?

### A.2 Main Interview Questions Part 1

• What industry is your company/employer in?

• How big is the company you are working in?

• How big is your team or teams that you typically work with?

• What is your typical role in a UX project?

• In your company, are there any company-wide or team-wide policies around AI tools and their use? What are they?

• Were there any concerns or hesitations within the company or your teams regarding the decision to integrate AI in the workflow?

– What were the thoughts and attitudes regarding using AI?

• Have you or your team used AI in any part of your UX projects? How?

### A.3 Main Interview Questions Part 2A (if the

interviewee or their team have used AI)

• Name the tools you use or have used

• In which steps of the process do you integrate AI in your work?

• How many people in your team(s) are using AI in your cur- rent projects? For example, are there specific roles that use AI a lot, or some roles that don’t?

• Can you walk me through your main steps in your and your team’s workflow when you are using AI tools in your projects?

– How frequently does AI come into play in your current work?

• So Can you walk me through the same workflow in a tradi- tional way without getting an AI assistant/the specific tools? How did you work on projects before AI?

• What were your first experiences like when using AI tools in your work? What challenges did you face, and is there anything you wish you knew or understood at the time?

• To what extent do you trust the AI tools and their outcomes? What kind of a role does AI serve in your decision-making processes? Do you often edit the outcomes or check them for correctness and quality?

• Considering the above questions, is your approach in using AI tools, aligned with the company/team approach? In other words, are the decisions to experiment and adopt AI tools in work, made individually, or internally in teams, or does the company decide and provide the tool(s) for the team?

– If it is a team or company approach to use the tool, are you obligated to follow the design process with AI tools, or is it just an option?

– If it is for individual purposes or within teams, do you think the company is against it, or doesn’t matter? Are they aware of the use of all AI tools?

– Are there any employees that hesitate or refuse to use AI tools that you or your company would like to use? If so, what are their reasons?

• What benefits do you think you get out of using AI tools in your work?

• Are you going to use AI tools again in your future projects? Are there any ways in which you or your team or company is looking to change the use of AI tools?

### A.4 Main Interview Questions Part 2B (if the

interviewee or their team have not used AI)

• Are there any particular reasons for why you and/or your team or company are not using AI tools?

– Was that a personal decision or obligated by the team or

– Did you or do you personally have such concerns or hesi-

company?

tations?

– Have there been discussions about it at your workplace?

– Did the thoughts/attitudes/concerns impact the decision-

– What are your coworkers’ and team members’ attitudes

making process at different levels of the company?

about using AI?

• Have you or your team tried using any AI tools? If so, what was the outcome, and did that play into your decision to not use AI tools?

• (if they have experience) What were your first experiences like when using AI tools in your work? What challenges and hesitations? did you face, and is there anything you wish you knew or understood at the time?

• Can you walk me through the design process for a typical project that you have worked or are currently working on?

– What are the typical challenges or obstacles you face in your UX projects?

• What would need to change so that you and your team would begin to use AI tools in your work?

### A.5 Main Interview Questions Part 3 (regardless of prior AI use)

• What in your opinion are the greatest strengths of AI and AI tools?

• What in your opinion are the greatest challenges of AI and AI tools?

• How do you see your work and work practices changing within the next five years?

• Do you have any suggestions for us to focus on in our re- search?

• Is there anything else you want to add to your session?

• Is there any question that you think I should have asked that I didn’t?