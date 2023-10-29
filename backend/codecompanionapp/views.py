from django.shortcuts import  render, redirect
from codecompanionapp.signUpForm import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CodeCompanionUserSerializer
from .models import CodeCompanionUser
from codecompanionapp import JavaFiles, PythonFiles, FilesHandler, ftCodeOptimizer, ftDocumentationHelper, ftCodeDebugger, ftCodeReviewer, ftCommentGenerator, ftLearningPathRecommendations, ftLetterGenerator, ftResumeFilterer, ftSummarizeAppraisals, ftTechnicalTrends, ftUnitTestGenerator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Test View
class CodecompanionView(viewsets.ModelViewSet):
    serializer_class = CodeCompanionUserSerializer
    queryset = CodeCompanionUser.objects.all()

app_home = "homepage"
def homepage(request):
	return render(request=request, template_name='codecompanionapp/home.html')
@csrf_exempt
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(app_home)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="codecompanionapp/registerationPage.html", context={"registration_form":form})

@csrf_exempt
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(app_home)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="codecompanionapp/loginPage.html", context={"login_form":form})
	
@csrf_exempt
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect(app_home)
@csrf_exempt
def code_debugger(request):
	if request.method == "POST":
		form = ftCodeDebugger.CodeDebuggerForm(request.POST, request.FILES)
		if form.is_valid():
			if request.FILES:
				file_name = request.FILES['input_file'].name
				if file_name.endswith(JavaFiles.JavaFile.get_file_type()):
					input_file = JavaFiles.JavaFile.read_file(request.FILES.get('input_file', ""))
				elif file_name.endswith(PythonFiles.PythonFile.get_file_type()):
					input_file = PythonFiles.PythonFile.read_file(request.FILES.get('input_file', ""))
				else:
					input_file = ""
			else:
				input_file = ""
			input_code = form.cleaned_data.get('input_code')
			responseFromLLM = form.generate_chat_completion(input_file, input_code)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftCodeDebugger.CodeDebuggerForm()
	return render(request=request, template_name="codecompanionapp/codeDebugger.html", context={"codeDebugger_form":form})

@csrf_exempt
def code_optimizer(request):
	if request.method == "POST":
		form = ftCodeOptimizer.CodeOptimizerForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			responseFromLLM = form.generate_chat_completion(input_code)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftCodeOptimizer.CodeOptimizerForm()
	return render(request=request, template_name="codecompanionapp/codeOptimizer.html", context={"codeOptimizer_form":form})
@csrf_exempt
def code_reviewer(request):
	if request.method == "POST":
		form = ftCodeReviewer.CodeReviewerForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			responseFromLLM = form.generate_chat_completion(input_code)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftCodeReviewer.CodeReviewerForm()
	return render(request=request, template_name="codecompanionapp/codeReviewer.html", context={"codeReviewer_form":form})
@csrf_exempt
def comment_generator(request):
	if request.method == "POST":
		form = ftCommentGenerator.CommentGeneratorForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			responseFromLLM = form.generate_chat_completion(input_code)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftCommentGenerator.CommentGeneratorForm()
	return render(request=request, template_name="codecompanionapp/commentGenerator.html", context={"commentGenerator_form":form})
@csrf_exempt
def documentation_helper(request):
	if request.method == "POST":
		form = ftDocumentationHelper.DocumentationHelperForm(request.POST, request.FILES)
		if form.is_valid():
			if request.FILES:
				input_file = FilesHandler.FileHandler.read_file(request.FILES.get('input_file', ""))
			else:
				input_file = ""
			input_code = form.cleaned_data.get('input_code')
			responseFromLLM = form.generate_chat_completion(input_file, input_code)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftDocumentationHelper.DocumentationHelperForm()
	return render(request=request, template_name="codecompanionapp/documentationHelper.html", context={"documentationHelper_form":form})
@csrf_exempt
def learning_path_recommendation(request):
	if request.method == "POST":
		form = ftLearningPathRecommendations.LearningPathRecommendationsForm(request.POST)
		if form.is_valid():
			input_current_designation = form.cleaned_data.get('input_current_designation')
			input_current_expertise = form.cleaned_data.get('input_current_expertise')
			responseFromLLM = form.generate_chat_completion(input_current_expertise, input_current_designation)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftLearningPathRecommendations.LearningPathRecommendationsForm()
	return render(request=request, template_name="codecompanionapp/learningPathRecommendations.html", context={"learningPathRecommendations_form":form})

@csrf_exempt
def letter_generator(request):
	if request.method == "POST":
		form = ftLetterGenerator.LetterGeneratorForm(request.POST)
		if form.is_valid():
			input_name = form.cleaned_data.get('input_name')
			input_type_of_letter = form.cleaned_data.get('input_type_of_letter')
			input_extra_details = form.cleaned_data.get('input_extra_details')
			input_organisation_details = form.cleaned_data.get('input_organisation_details')
			input_designation = form.cleaned_data.get('input_designation')
			responseFromLLM = form.generate_chat_completion(input_name, input_type_of_letter, input_extra_details, input_organisation_details, input_designation)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftLetterGenerator.LetterGeneratorForm()
	return render(request=request, template_name="codecompanionapp/letterGenerator.html", context={"letterGenerator_form":form})

def resume_filterer(request):
	if request.method == "POST":
		form = ftResumeFilterer.ResumeFiltererForm(request.POST, request.FILES)
		if form.is_valid():
			input_file1 = FilesHandler.FileHandler.read_file(request.FILES.get('input_file1'))
			input_file2 = FilesHandler.FileHandler.read_file(request.FILES.get('input_file2'))
			input_file3 = FilesHandler.FileHandler.read_file(request.FILES.get('input_file3', ""))
			input_file = input_file1 + '\n' + input_file2 + '\n' + input_file3
			input_message = form.cleaned_data.get('input_job_role')
			responseFromLLM = form.generate_chat_completion(input_file, input_message)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftResumeFilterer.ResumeFiltererForm()
	return render(request=request, template_name="codecompanionapp/resumeFilterer.html", context={"resumeFilterer_form":form})


def summarize_appraisals(request):
	if request.method == "POST":
		form = ftSummarizeAppraisals.SummarizeAppraisalsForm(request.POST, request.FILES)
		if form.is_valid():
			if request.FILES:
				input_file = FilesHandler.FileHandler.read_file(request.FILES.get('input_file', ""))
			else:
				input_file = ""
			input_appraisal = form.cleaned_data.get('input_appraisal')
			responseFromLLM = form.generate_chat_completion(input_file, input_appraisal)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftSummarizeAppraisals.SummarizeAppraisalsForm()
	return render(request=request, template_name="codecompanionapp/summarizeAppraisals.html", context={"summarizeAppraisals_form":form})

def technical_trends(request):
	if request.method == "POST":
		form = ftTechnicalTrends.TechnicalTrendsForm(request.POST)
		if form.is_valid():
			input_domain = form.cleaned_data.get('input_domain')
			responseFromLLM = form.generate_chat_completion(input_domain)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftTechnicalTrends.TechnicalTrendsForm()
	return render(request=request, template_name="codecompanionapp/technicalTrends.html", context={"technicalTrends_form":form})

def unit_test_generator(request):
	if request.method == "POST":
		form = ftUnitTestGenerator.UnitTestGeneratorForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			responseFromLLM = form.generate_chat_completion(input_code)
			return render(request=request, template_name="codecompanionapp/output.html", context={"response": responseFromLLM})
	form = ftUnitTestGenerator.UnitTestGeneratorForm()
	return render(request=request, template_name="codecompanionapp/unitTestGenerator.html", context={"unitTestGenerator_form":form})



#messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
