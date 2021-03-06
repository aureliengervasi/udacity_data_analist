#P7 - Design an A/B test

## Motivation

This work is part of the Udacity Data Analyst Nanoprogram. This is the final project for the course on A/B testing. The goal of this project is to design an A/B test in order modify the Udacity website to improve the overall student experience and improve coaches' capacity to support students.

## Experiment Overview: Free Trial Screener

At the time of this experiment, Udacity courses currently have two options on the home page: "start free trial", and "access course materials". If the student clicks "start free trial", they will be asked to enter their credit card information, and then they will be enrolled in a free trial for the paid version of the course. After 14 days, they will automatically be charged unless they cancel first. If the student clicks "access course materials", they will be able to view the videos and take the quizzes for free, but they will not receive coaching support or a verified certificate, and they will not submit their final project for feedback.

In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. This screen-shot shows what the experiment looks like.

The hypothesis was that this might set clearer expectations for students upfront, thus reducing the number of frustrated students who left the free trial because they didn't have enough time—without significantly reducing the number of students to continue past the free trial and eventually complete the course. If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.

The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

## Metric Choice

The following metrics were available as invariant or evaluation metrics.

The practical significance boundary for each metric, that is, the difference that would have to be observed before that was a meaningful change for the business, is given in parentheses. All practical significance boundaries are given as absolute changes.

### Invariant metrics

- **Number of cookies**: *number of unique cookies to view the course overview page.* (dmin=3000)

This metric should not significantly change with the new free trial screener. This is an estimation of the number of unique visitors on the course overview. As it pops up after clicking on "start free trial", the trial screener does not impact this page. 

- **Number of clicks**: *number of unique cookies to click the "Start free trial" button (which happens before the free trial screener is trigger)*. (dmin=240)

For the same reasons, as above, the trial screener should not impact this metrics. 

- **Click-through-probability**: *number of unique cookies to click the "Start free trial" button divided by number of unique cookies to view the course overview page.*(dmin=0.01)

This metric being a combination of the two previous invariant metrics, it should also stay invariant throughout the experiment.

### Evaluation metrics

- **Gross conversion**: *number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button.* (dmin= 0.01)

If the trial screener works as expected, fewer visitors will enroll in the free trial because some of them will prefer to stick with the free course material. And as the number of unique cookies to click the "start free trial" button should not significantly change; this metric should be lower for the experiment group than for the control group.

- **Net conversion**: *number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button.* (dmin= 0.0075)

One of the goal of this experiment is to show that, even with the trial screener, the number of students that stay enrolled after the 14-day boundary is not reduced. To validate this assumption, this metric should not decrease significantly.

Another solution could have been to have also chosen the retention metric, but as its probability is close to 50%, it would lead to a very high number of page views to spot significant changes.


### Unused metrics

- **Number of user-ids**: *number of users who enroll in the free trial.* (dmin=50)

This metric could have been chosen as an evaluation metric, as the experiment is supposed reduce it significantly. But as it is an absolute value, and not a ratio, its variation also depends on the number of students that ends up in the group. This dependency makes it a relatively poor evaluation metrics to my opinion.


- **Retention**: *number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout.* (dmin=0.01)

This metric could have been used as an evaluation metrics. We could logically expect that it would increase, as the students who enroll are more likely to remain enrolled past the 14-day boundary.

But as its baseline value is close to 0.5 (0.53), it would lead to a very high number of samples (4 655 238 page views without the Bonferroni correction!) to validate the test power.



## Measuring Standard Deviation

Baseline values for some metrics are given in the table below:

Metric | Baseline values
------------ | -------------
Click-through-probability on "Start free trial": | 0.08
Probability of enrolling, given click: | 0.20625
Probability of payment, given click | 0.1093125

To estimate each evaluation metric standard deviation, I will use an assumption about their underlying distribution; I will assume that they follow a binomial distribution law. This will permit me to derive analytically each metric standard deviation.

Sample size visiting the course overview page: 5000 cookies

Evaluation metric | Sample size | Probability | Standard deviation
------------ | ------------- | ------------- | -------------
Gross conversion | 400 | 0,21 | 0,0202
Net conversion | 400 | 0,11 | 0,0156

All the chosen evaluation metrics are probabilities where the unit of analysis is a count of cookies. In our experiment, the unit of diversion is also the cookie. Hence, we can be confident in using this analytical method to estimate the variability.

But it is important to note that assuming these distributions to be like binomial distributions involves a chance that their variability gets underestimated. 

Following Google's common practice, conducting A/A experiments on these metrics would be a good solution to get their variability empirically. 

If possible, I would conduct empirical variability estimations on both metrics because, due to the low click-through probability, each page view refers to a very limited number of samples (roughly 400). Hence, there is a chance that variability gets underestimated analytically. 

## Sizing

### Problem formulation 

To clarify the problem, I detailed below the chosen Null hypothesis and how do we reject it.

**Null hypothesis**: The trial screener does not reduce the number of frustrated students who leave the free trial or the trial screener reduces the number of students continuing past the free trial.

So, to reject the Null hypothesis, the following alternative hypothesis must be validated:
- There is a significant reduction of the gross conversion rate, 

**AND**

- There is not a significant reduction of the net conversion rate

I will not use the Bonferroni correction on these two metrics because the **AND** relation that binds them is conservative enough. 


### Number of Samples vs. Power

**NB:** to get the total page view number, we need the maximum number of samples related to one metric, multiply it by the click-through probability to get the number of pages, and multiply it by 2 to get the total number of pages for both groups (experiment and control)


Evaluation metrics | probability = p | dmin | α | 1−β | Total page views
------- | -------- | -------- | -------- | -------- | --------
Gross conversion | 0,21 | 0,01 | 5% | 80% | 651075
Net conversion | 0,11 | 0,0075 | 5% | 80% | 683050

Approximately 683050 page views will be needed for this experiment.

### Duration vs. Exposure

This amount of page views can be obtained in less than 18 days if 100% of the traffic is dedicated to this experiment. 

Supposing that no other experiment is being run at the same time, this could be an acceptable solution. 

This choice can be justified by the fact that the users participating in this experiment are exposed to minimal risk. They are no chance that people gets hurt (physically, nor psychologically, nor emotionally), or that sensitive personal data gets leaked. It does not seem necessary to limit this experiment to a fraction of the total traffic.

But dedicating all the website traffic to this experiment can also lead to strong disturbances if something goes wrong in the implementation. For instance, we can lose up to 50% of the users (the experiment group) willing to register for the free trial. But as the website modification is small, this is quite unlikely.


## Analysis

### Sanity check

Out of the [first results](https://docs.google.com/spreadsheets/d/1Mu5u9GrybDdska-ljPXyBjTpdZIUev_6i7t4LRDfXM8/edit#gid=0), sanity checks on the invariants metrics must be done to verify that our experiment is not significantly changing some key metrics. 

#### Number of cookies

What we expect to see is that these cookies should be allocated with a statistical probability of 0.5 between the control group and the experiment group. So, to pass the test, we need to verify that the ratio of cookies allocated in the control group lies in a 95% confidence interval of a similar distribution following a binomial law of probability 0.5.
 
Indicator | Value
---- | ----
Expected ratio: | 0.5
Confidence interval (binomial distribution) | [0.4988; 0.5012]
Observed ratio: | 0.5006
Sanity check: | **Passed!**

#### Number of clicks on the "Start free trial" button

As for the previous metric, we expect to see that these clicks should be equally distributed with a statistical probability of 0.5 between the control group and the experiment group. So, to pass the test, we need to verify that the ratio of clicks allocated in the control group lies in a 95% confidence interval of a similar distribution following a binomial law of probability 0.5.
 
Indicator | Value
---- | ----
Expected ratio: | 0.5
Confidence interval (binomial distribution) | [0.4959; 0.5041]
Observed ratio: | 0.5005
Sanity check: | **Passed!**

#### Click-through-probability (CTP) on the "Start free trial" button

For this metric, we need to check if the CTP difference between the two groups lies in the 95% confidence interval of the pooled distribution. 

Indicator | Value
---- | ----
Expected difference: | 0.0
Confidence interval | [-0.0013; 0.0013]
Observed ratio: | 0.0001
Sanity check: | **Passed!**

### Result analysis

A metric is statistically significant if the confidence interval does not include 0 (that is, you can be confident there was a change), and it is practically significant if the confidence interval does not include the practical significance boundary (that is, you can be confident there is a change that matters to the business.)


#### Gross conversion

This metric must be significantly different between the control group and the experiment group to reject our Null hypothesis. We are using the pooled standard error to estimate the 95% confidence interval (no Bonferroni correction).

Indicator | Value
---- | ----
Pooled standard error | 0.0044
Observed difference | -0.0206
Confidence interval | [-0.0291; -0.0120]
Statistical significance: | **Yes**
Practical significance boundary | 0.010
Practical significance: | **Yes**

#### Net conversion

This metric should **NOT** decrease significantly between the control group and the experiment group to reject our Null hypothesis. Indeed, we don't want our net conversion to decrease with the new free trial screener. As before, we are using here the pooled standard error to estimate the 95% confidence interval (no Bonferroni correction).

Indicator | Value
---- | ----
Pooled standard error | 0.0034
Observed difference | -0.0049
Confidence interval | [-0.0116; 0.0019]
Statistical significance: | **No**
Practical significance boundary | 0.0075
Practical significance: | **No**

It is important to underline the fact that the lower bound of the practical significance interval (-0.0075) is included in the confidence interval [-0.0116; 0.0019]. This means that we cannot state that the free-trial screener does not reduce the net retention level past the practical significance level.

### Sign test

We can also conduct a sign-test with the day-by-day data. In this case, we count the number of events where the metrics difference between the two groups is negative (or positive). We then compare this scenario with the one of a binomial distribution with probability 0.5. This gives us the probability that this scenario happens only "by chance". 

#### Gross conversion

Indicator | Value
---- | ----
Number of positive events | 19
Total number of events | 23
Two-tail p-value (binomial distribution) | 0.0026
Statistical significance? | **Yes**

#### Net conversion

Indicator | Value
---- | ----
Number of positive events | 13
Total number of events | 23
Two-tail p-value (binomial distribution) | 0.6776
Statistical significance? | **No**

### Summary

The effect-size hypothesis test and the sign-test both showed from the first results that there the gross conversion should significantly be reduced by the change.

But the net conversion metrics still hold uncertainties whether it will not decrease with the new screener.  

As we are testing whether the gross conversion is reduced, **AND** that the net conversion is not reduced, I did not use the Bonferroni correction. Otherwise, it would have been too conservative and would have increase the chance of false negative.  

## Recommendation

Out of the first results, all the sanity checks on the invariant metrics have been validated. When looking at the evaluation metrics, the gross conversion shows a significant (statistically and practically) reduction.

But the net conversion metrics only shows that there is no statistically significant change. The lower bound of the practical significance interval is included in the confidence interval. This means that we cannot ensure yet (with alpha = 95%) that the net conversion will not decrease beyond the practical significance boundary. We need more samples to precise our confidence interval.

This would be a good time to get the client's opinion. What the first results showed us is that:
- the free-trial screener significantly reduces the gross conversion, which could be translated in a cost reduction for our client
- the free trial screener will not significantly increase the net conversion, and there is a slight chance that it can even decrease it, resulting in a loss of income.

What is difficult for me to assess, is whether the cost reduction caused by the free-trial screener could easily compensate the potential loss of income. If this is the case, I would recommend to launch the experiment, which could help us to get more samples and precise our confidence interval for the net conversion. Otherwise, it would be wiser to think about another experiment. 


# Follow-up experiment

To reduce further the number of frustrated students who cancel in early course, another experiment could be conducted. 

To keep student motivation during the free trial process, an e-mail could be send to them if they have not logged in for 4 days. This e-mail could remind them that improvement comes with regular work, it could also give a motivational speech reminding them what job opportunities may be offered to them if they finish the program. 

My hypothesis in this case would be that sending this e-mail would help to reduce the number of students having already enrolled in the free trial program and canceling before the end of the 14-day boundary.

I would use the retention as an evaluation metric.

>That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout.

As our experiment is dealing with users having already enrolled, it does not make sense anymore to use cookie-based metrics. In this case, my unit of diversion would be the user-id. 

I would expect the retention to be significantly higher in the experiment group than in the control group. With this metric, I will be able to detect if this e-mail sending improves the number of students continuing after the 14-day boundary. 

But using the retention metrics might lead to a high number of necessary page views as its baseline value is close to 0.5. We need to make sure that the test duration is compatible with the business needs.

My unit of diversion being the user-id, I would use the number of user-id as an invariant metrics to conduct my sanity checks.

