t1 = ['courses', 'electromagnetic waves', 'linearity', 'current density', 'alpha u1', 'times', 'b2', 'laughs', 'solutions', 'today', 'chromodynamics', 'tau', 'b1', 'later courses', 'radio stations', 'densities', 'superposition', 'conversations', 'tau au', 'quantum chromodynamics', 'charged densities', 'schrodinger', 'situation', 'j1', 'electrodynamics', 'du dt', 'lu1', 'heisenberg', 'quantum gravity', 'j2', 'dynamical variables', 'semester', 'mechanics', 'e2', 'quantum mechanics', 'example', 'e1', 'thoughts', 'string theory', 'l1', 'u1', 'transmitting stations', 'physics', 'general relativity', 'vu vt', 'beta u2', 'u2', 'quantum physics', 'classical physics', 'fundamental theory']
# t2 = ['operator', 'advantage', 'acceleration', 'motion', 'vector', 'fact', 'space', 'things', 'number', 'time', 'argument', 'equation', 'derivatives', 'influence', 'new solutions', 'problem', 'numbers', 'equations', 'course', 'linear', 'dimensions', 'structure', '1d', 'necessity', 'answer', 'quantum', 'times', 'position', 'value', 'particle', 'partial derivative', 'probabilities', 'schrodinger', 'relativity', 'theory', 'superpositions', 'semester', 'newton', 'mathematics', 'functions', 'psi', 'interpretation', 'dynamics', 'complex numbers', 'physics', 'solutions', 'ddt', 'classical mechanics', 'mechanics', 'quantum mechanics']
# t3 = ['lot', 'electromagnetism', 'conjugate', 'thing', 'things', 'star', 'importance', 'fact', 'projection', 'quantum', 'numbers', 'ideas', 'identity', 'physicists', 'axis', 'systems', 'radius', 'bit', 'square', 'discovery', 'end', 'velocity', 'discoveries', 'equation', 'einstein', 'max born', 'cosine', 'probabilities', 'equations', 'maybe ib', 'position', 'unit radius', 'complex numbers', 'solutions', 'quantum mechanics', 'silly reasons', 'idea', 'ib', 'interpretation', 'ammeter', 'amazing discoveries', 'theta', 'square root', 'paper', 'cosine theta', 'classical mechanics', 'times', 'schrodinger', 'mechanics', 'psi']

# original goal: get frequency of words across all data sets using tf-idf to create a general large data set of keywords for quantum mechanics
# problem: the data sets don't have many words in common, so checking for the frequency of a word across all data sets won't have much benefit
# compromise: have a separate keywords dataset for each video and check for timestamp importance that way

# text_1_with_time_stamps = ("0:00 Very good. 0:02 So it's time to start. 0:04 So today, I want to talk about general features of quantum 0:08 mechanics. 0:10 Quantum mechanics is something that takes some time to learn, 0:14 and we're going to be doing some of that learning this semester. 0:18 But I want to give you a perspective of where we're 0:22 going, what are the basic features, how 0:25 quantum mechanics looks, what's surprising about it, 0:29 and introduce some ideas that will 0:33 be relevant throughout this semester and some 0:36 that will be relevant for later courses as well. 0:40 So it's an overview of quantum mechanics. 0:43 So quantum mechanics, at this moment, 0:46 is almost 100 years old. 0:50 Officially-- and we will hear-- 0:53 this year, in 2016, we're celebrating the centenary 0:59 of general relativity. 1:01 And when will the centenary of quantum mechanics be? 1:06 I'm pretty sure it will be in 2025. 1:10 Because in 1925, Schrodinger and Heisenberg 1:16 pretty much wrote down the equations of quantum mechanics. 1:21 But quantum mechanics really begins earlier. 1:25 The routes that led to quantum mechanics began in the late 1:32 years of the 19th century with work of Planck, 1:37 and then at the beginning of the century, 1:39 with work of Einstein and others,m as we will see today 1:44 and in the next few lectures. 1:46 So the thoughts, the puzzles, the ideas 1:51 that led to quantum mechanics begin before 1925, 1:56 and in 1925, it suddenly happened. 1:58 So what is quantum mechanics? 2:02 Quantum mechanics is really a framework to do physics, 2:06 as we will understand. 2:07 So quantum physics has replaced classical physics 2:13 as the correct description of fundamental theory. 2:18 So classical physics may be a good approximation, 2:22 but we know that at some point, it's not quite right. 2:26 It's not only not perfectly accurate. 2:29 It's conceptually very different from the way things 2:35 really work. 2:36 So quantum physics has replaced classical physics. 2:40 And quantum physics is the principles 2:44 of quantum mechanics applied to different physical phenomena. 2:50 So you have, for example, quantum electrodynamics, 2:54 which is quantum mechanics applied to electromagnetism. 2:58 You have quantum chromodynamics, which 3:01 is quantum mechanics applied to the strong interaction. 3:05 You have quantum optics when you apply quantum mechanics 3:09 to photons. 3:10 You have quantum gravity when you 3:13 try to apply quantum mechanics to gravitation. 3:18 Why the laughs? 3:21 And that's what gives rise to string theory, which 3:26 is presumably a quantum theory of gravity, 3:30 and in fact, the quantum theory of all interactions 3:32 if it is correct. 3:34 Because it not only describes gravity, 3:36 but it describes all other forces. 3:39 So quantum mechanics is the framework, 3:44 and we apply it to many things. 3:46 So what are we going to cover today? 3:49 What are we going to review? 3:50 Essentially five topics-- one, the linearity 3:59 of quantum mechanics, two, the necessity of complex numbers, 4:14 three, the laws of determinism, four, 4:25 the unusual features of superposition, 4:41 and finally, what is entanglement. 4:45 4:52 So that's what we aim to discuss today. 4:58 So we'll begin with number one, linearity. 5:04 And that's a very fundamental aspect 5:08 of quantum mechanics, something that we have 5:11 to pay a lot of attention to. 5:13 So whenever you have a theory, you 5:17 have some dynamical variables. 5:19 These are the variables you want to find 5:22 their values because they are connected with observation. 5:26 If you have dynamical variables, you 5:29 can compare the values of those variables, 5:33 or some values deduced from those variables, 5:36 to the results of an experiment. 5:38 So you have the equations of motion, so linearity. 5:42 We're talking linearity. 5:47 You have some equations of motion, EOM. 5:53 And you have dynamical variables. 6:00 If you have a theory, you have some equations, 6:04 and you have to solve for those dynamical variables. 6:08 And the most famous example of a theory that is linear 6:14 is Maxwell's theory of electromagnetism. 6:18 Maxwell's theory of electromagnetism 6:20 is a linear theory. 6:22 What does that mean? 6:24 Well, first, practically, what it means 6:26 is that if you have a solution-- 6:29 for example, a plane wave propagating in this direction-- 6:35 and you have another solution-- 6:38 a plane wave propagating towards you-- 6:42 then you can form a third solution, 6:46 which is two plane waves propagating simultaneously. 6:52 And you don't have to change anything. 6:54 You can just put them together, and you get a new solution. 6:59 The two waves propagate without touching each other, 7:03 without affecting each other. 7:07 And together, they form a new solution. 7:10 This is extraordinarily useful in practice 7:14 because the air around us is filled 7:17 with electromagnetic waves. 7:19 All your cell phones send electromagnetic waves 7:24 up the sky to satellites and radio stations 7:28 and transmitting stations, and the millions of phone calls 7:33 go simultaneously without affecting each other. 7:37 A transatlantic cable can conduct millions of phone calls 7:43 at the same time, and as much data and video and internet. 7:49 It's all superposition. 7:51 All these millions of conversations 7:54 go simultaneously through the cable 7:56 without interfering with each other. 8:00 Mathematically, we have the following situation. 8:04 In Maxwell's theory, you have an electric field, 8:11 a magnetic field, a charge density, and a current density. 8:17 8:20 That's charge per unit area per unit of time. 8:25 That's the current density. 8:27 And this set of data correspond to a solution 8:33 if they satisfy Maxwell's equations, 8:37 which is a set of equations for the electromagnetic field, 8:41 charged densities, and current density. 8:43 So suppose this is a solution, that you verify that it 8:47 solves Maxwell's equation. 8:50 Then linearity implies the following. 8:58 You multiply this by alpha, alpha e, alpha b, alpha rho, 9:08 and alpha j. 9:11 And think of this as the new electric field, 9:13 the new magnetic field, the new charged density, 9:16 and the new current is also a solution. 9:18 9:25 If this is a solution, linearity implies 9:32 that you can multiply those values 9:35 by a number, a constant number, a alpha being a real number. 9:42 9:45 And this is still a solution. 9:48 It also implies more. 9:49 Linearity means another thing as well. 9:52 It means that if you have two solutions, e1, b1, rho 1, j1, 10:01 and e2, b2, rho 2, j2-- 10:08 10:11 if these are two solutions, then linearity 10:25 implies that the sum e1 plus e2, b1 plus b2, rho 1 plus rho 2, 10:37 and j1 plus j2 is also a solution. 10:44 10:54 So that's the meaning, the technical meaning of linearity. 11:00 We have two solutions. 11:02 We can add them. 11:03 We have a single solution. 11:04 You can scale it by a number. 11:07 Now, I have not shown you the equations 11:11 and what makes them linear. 11:13 But I can explain this a little more as to 11:17 what does it mean to have a linear equation. 11:21 Precisely what do we mean by a linear equation? 11:24 So a linear equation. 11:26 11:30 And we write it schematically. 11:32 We try to avoid details. 11:34 We try to get across the concept. 11:37 A linear equation, we write this l u equal 0 where 11:47 u is your unknown and l is what is called the linear operator, 12:00 something that acts on u. 12:03 And that thing, the equation, is of the form l and u equal 0. 12:09 Now, you might say, OK, that already 12:12 looks to me a little strange, because you have just one 12:15 unknown, and here we have several unknowns. 12:19 So this is not very general. 12:21 And you could have several equations. 12:23 Well, that won't change much. 12:26 We can have several linear operators 12:31 if you have several equations, like l1 or something, 12:35 l2 on something, all these ones equal to 0 12:40 as you have several equations. 12:42 So you can have several u's or several unknowns, 12:46 and you could say something like you have l on u, v, 12:53 w equals 0 where you have several unknowns. 12:59 But it's easier to just think of this first. 13:02 And once you understand this, you can think about the case 13:05 where you have many equations. 13:07 So what is a linear equation? 13:11 It's something in which this l-- 13:15 the unknown can be anything, but l 13:17 must have important properties, as being a linear operator 13:22 will mean that l on a times u, where a is a number, 13:29 should be equal to alu and l on u1 plus u2 on two unknowns 13:41 is equal to lu 1 lu 2. 13:46 This is what we mean by the operator being linear. 13:50 13:54 So if an operator is linear, you also 13:58 have l on alpha u1 plus beta u2. 14:06 You apply first the second property, l on the first plus 14:09 l on the second. 14:11 So this is l of alpha u1 plus l of beta u2. 14:19 And then using the first property, 14:22 this is alpha l of u1 plus beta l of u2. 14:29 And then you realize that if u1 and u2 are solutions-- 14:41 which means lu 1 equal lu 2 equals 0 14:47 if they solve the equation-- 14:49 then alpha u1 plus beta u2 is a solution. 14:58 15:02 Because if lu1 is 0 and lu2 is 0, l of alpha u1 plus beta u2 15:10 is 0, and it is a solution. 15:13 So this is how we write a linear equation. 15:23 Now, an example probably would help. 15:27 If I have the differential equation 15:30 du dt plus 1 over tau u equals 0, 15:39 I can write it as an equation of the form lu 15:45 equals 0 by taking l on u to be defined 15:51 to be vu vt plus 1 over tau u. 15:59 Now, it's pretty much-- 16:02 I haven't done much here. 16:03 I've just said, look, let's define l [? active ?] [? on ?] 16:07 u to be this. 16:09 And then certainly, this equation is just lu equals 0. 16:13" \
#                           "The question would be maybe if somebody would tell you 16:17 how do you write l alone-- 16:20 well, l alone, probably we should write it 16:24 as d dt without anything here plus 1 over tau. 16:32 Now, that's a way you would write 16:35 it to try to understand yourself what's going on. 16:37 And you say, well, then when l acts as the variable u, 16:41 the first term takes the derivative, 16:44 and the second term, which is a number, just multiplies it. 16:48 So you could write l as this thing. 16:52 And now it is straightforward to check 17:00 that this is a linear operator. 17:03 l is linear. 17:08 And for that, you have to check the two properties there. 17:11 So for example, l on au would be ddt of au 17:20 plus 1 over tau au, which is a times du d tau 17:28 plus 1 over tau u, which is alu. 17:32 17:34 And you can check. 17:35 I asked you to check the other property 17:38 l on u1 plus u2 is equal to lu 1 plus lu 2. 17:46 Please do it. ").split(" ")

with open("text1_ts.txt", "r+", encoding="utf-8") as f:
    transcript = f.read().split("\n")

# print(transcript)
dct = {}
for i, element in enumerate(transcript):
    try:
        print(int(element[0]))
    except ValueError:
        for keyword in t1:
            if keyword in element:
                dct[transcript[i-1]] = 1
                break
            else:
                dct[transcript[i-1]] = 0
print(dct)