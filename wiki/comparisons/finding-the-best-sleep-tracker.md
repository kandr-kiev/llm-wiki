---
title: "finding the best sleep tracker"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - application
  - best-practice
  - data
  - image-generation
  - open-source
  - prompt-tuning
  - real-time
---# finding the best sleep tracker

> **Source:** finding-the-best-sleep-tracker-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** [ #  karpathy ](/) Home Blog # Finding the Best Sleep Tracker * 24 Mar, 2025 * About 2 months ago I stumbled by this Bryan Johnson video on How I FIXED My Terrible Sleep - 10 Habits. I resolved that d...
> **Sources:**
>   - finding-the-best-sleep-tracker-2026-07-10.md
> **Links:**
- [[auto-grade-hn]]
- [[chemical-hygiene]]
- [[animals-vs-ghosts]]
- [[away]]
- [[automating-ai-away-2026-07-07]]

## Key Findings

[
# 
karpathy
](/)
Home Blog
# Finding the Best Sleep Tracker
*
24 Mar, 2025
*
About 2 months ago I stumbled by this Bryan Johnson video on How I FIXED My Terrible Sleep - 10 Habits. I resolved that day to listen to Bryan and try to improve my sleep. But before we can improve it, first - how should we measure it? Bryan Johnson seems to use Whoop, but at that time I only had my Apple Watch (coupled with one of the popular sleep apps - AutoSleep). And then a long time ago I used and liked Oura. And I also had an order in for the new and fancy 8Sleep Pod 4 Ultra, which I was aware offers some sleep tracking too. So I found myself in a bit of a pickle - which one should I pick to track my sleep? And the answer of course is... to initiate a comprehensive tracking project to compare the 4 major candidates and find the. best. sleep. tracker. So that's what I did. This is me fully geared up and ready for bed:
![sleep_edit](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/sleep_edit.webp)
I've now gathered roughly 2 months of data. I kept the raw data in a simple spreadsheet, recording some of the basic measurements: the amount of sleep (Light, REM, Deep, and Awake tossing and turning), heart rate measurements (Resting Heart Rate (RHR), Heart Rate Variability (HRV)), and the sleep Score offered by each app. I'd log these every day right when I wake up so that I can compare and contrast the numbers and relate them to how I felt that morning. You can find my raw data in this spreadsheet, it looks like this:
![sleep_data](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/sleep_data.webp)
**Qualitative assessment**. Now, to spare you some suspense, after 2 months of data collection and staring at the results basically every morning, it was very pretty easy to guess that Oura and Whoop are both "Tier 1" - fairly similar and quite high quality in their sleep tracking. They both give similar scores that also correlated with the way I felt in the morning *most of the time*. Next is 8Sleep, which is ok. And finally, I was sad to learn that Apple Watch + AutoSleep (which I had used in the past for many months) was really, really terrible. Its scores are basically almost random and they swing around wildly, with little correlation to how I felt in the morning in comparison.
Let's now look at some of the data. First, let's look at the values that all 4 signals take on over the 2 months, with their histograms:
![signals](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/signals.webp)
As we can see, AutoSleep and 8Sleep are way too easy to please, giving out really high scores and pushing against the 100 score boundary. Whoop is also a little too easy to please, giving out 100 scores. Oura is the most difficult to please, shows a relatively nice gaussian distribution of scores, and offering the most dynamic range. I take this to be a good and nice property of Oura. Indeed, after 2 months my highest ever score on Oura was 92, while I ca

## Summary

n get 100 on Whoop fairly regularly. This means that I can keep going and striving for even more optimal sleep, one day.
Next, I was very curious about the correlation analysis between the trackers. We take all the scores and plot pairwise correlation scatter plots to see which of the trackers "agree the most" with each other. Here it is:
![corr](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/corr.webp)
And here are the correlations sorted:
Whoop vs Oura: 0.65
Oura vs 8Sleep: 0.59
Oura vs AutoSleep: 0.47
8Sleep vs AutoSleep: 0.42
Whoop vs 8Sleep: 0.38
Whoop vs AutoSleep: 0.14
Whoop and Oura seem to enjoy the highest correlation at ~0.65, while the other trackers are a bit all over the place. In particular, Whoop and AutoSleep are almost uncorrelated (0.14!). If we think that Whoop is good (which I think it is), AutoSleep looks almost like a noise generator.
**Matters of Heart Rate**. Next, I was interested to look at the Resting Heart Rate (RHR) and Heart Rate Variability (HRV). First, all trackers except 8Sleep agree quite highly on the heart rate during the night, including the Apple Watch. 8 Sleep is the worst because... it's a mattress so it doesn't have a direct measurement of the heart rate. I'm actually a bit impressed that it has a correlation this high:
AutoSleep 8Sleep Oura Whoop
AutoSleep 1.000000 0.947151 0.908987 0.942587
8Sleep 0.947151 1.000000 0.947977 0.878552
Oura 0.908987 0.947977 1.000000 0.904023
Whoop 0.942587 0.878552 0.904023 1.000000
Having established that all 3 devices (Oura, Whoop, AutoSleep) give a good and consistent measurement of resting heart rate during the night, I was curious if there is a correlation with the sleep score, as this is something Bryan mentioned a few times in his videos. In other words, is a lower RHR associated with better sleep score? Keep in mind that this is just correlation analysis, indeed, I have no idea if the apps take RHR as one of the measurements when they calculate the sleep score. For Whoop, it seems like there is a tiny bit of a correlation, i.e. lower RHR comes with higher sleep score (~0.13).
![whoopcorr](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/whoopcorr.webp)
But for Oura there is none:
![ouracorr](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/ouracorr.webp)
So... I'm not sure what to make of this. Going in, I thought that lower RHR would correlate quite well to better score but this doesn't seem to be the case.
Lastly, during the 2 months of data collection I was exercising regularly, getting about 30 minutes on average of Zone 2 cardio every day, except twice a week also doing a 4x4x4 HIIT (4 min off, 4 min on, 4 times). I was curious if this showed up and indeed it seems like it does, pretty cool:
![improvement](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/improvement.webp)
Using Whoop-Oura average measurement of both RHR and HRV, my resting heart rate has improved (decreased) by a bit less than 3 bpm over the 

## Related Articles

- [[auto-grade-hn]]
- [[chemical-hygiene]]
- [[animals-vs-ghosts]]
- [[away]]
- [[automating-ai-away-2026-07-07]]
