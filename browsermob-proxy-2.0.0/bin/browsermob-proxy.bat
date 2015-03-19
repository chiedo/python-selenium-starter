@REM ----------------------------------------------------------------------------
@REM Copyright 2001-2004 The Apache Software Foundation.
@REM
@REM Licensed under the Apache License, Version 2.0 (the "License");
@REM you may not use this file except in compliance with the License.
@REM You may obtain a copy of the License at
@REM
@REM      http://www.apache.org/licenses/LICENSE-2.0
@REM
@REM Unless required by applicable law or agreed to in writing, software
@REM distributed under the License is distributed on an "AS IS" BASIS,
@REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@REM See the License for the specific language governing permissions and
@REM limitations under the License.
@REM ----------------------------------------------------------------------------
@REM

@echo off

set ERROR_CODE=0

:init
@REM Decide how to startup depending on the version of windows

@REM -- Win98ME
if NOT "%OS%"=="Windows_NT" goto Win9xArg

@REM set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" @setlocal

@REM -- 4NT shell
if "%eval[2+2]" == "4" goto 4NTArgs

@REM -- Regular WinNT shell
set CMD_LINE_ARGS=%*
goto WinNTGetScriptDir

@REM The 4NT Shell from jp software
:4NTArgs
set CMD_LINE_ARGS=%$
goto WinNTGetScriptDir

:Win9xArg
@REM Slurp the command line arguments.  This loop allows for an unlimited number
@REM of arguments (up to the command line limit, anyway).
set CMD_LINE_ARGS=
:Win9xApp
if %1a==a goto Win9xGetScriptDir
set CMD_LINE_ARGS=%CMD_LINE_ARGS% %1
shift
goto Win9xApp

:Win9xGetScriptDir
set SAVEDIR=%CD%
%0\
cd %0\..\.. 
set BASEDIR=%CD%
cd %SAVEDIR%
set SAVE_DIR=
goto repoSetup

:WinNTGetScriptDir
set BASEDIR=%~dp0\..

:repoSetup


if "%JAVACMD%"=="" set JAVACMD=java

if "%REPO%"=="" set REPO=%BASEDIR%\lib

set CLASSPATH="%BASEDIR%"\etc;"%REPO%"\slf4j-api-1.7.7.jar;"%REPO%"\slf4j-jdk14-1.7.7.jar;"%REPO%"\sitebricks-0.8.9.jar;"%REPO%"\sitebricks-converter-0.8.9.jar;"%REPO%"\sitebricks-client-0.8.9.jar;"%REPO%"\xstream-1.3.1.jar;"%REPO%"\xpp3_min-1.1.4c.jar;"%REPO%"\sitebricks-annotations-0.8.9.jar;"%REPO%"\mvel2-2.1.3.Final.jar;"%REPO%"\guava-15.0.jar;"%REPO%"\annotations-7.0.3.jar;"%REPO%"\async-http-client-1.6.3.jar;"%REPO%"\netty-3.2.4.Final.jar;"%REPO%"\jsoup-1.5.2.jar;"%REPO%"\validation-api-1.0.0.GA.jar;"%REPO%"\guice-multibindings-3.0.jar;"%REPO%"\jackson-core-2.4.4.jar;"%REPO%"\jackson-databind-2.4.4.jar;"%REPO%"\jackson-annotations-2.4.0.jar;"%REPO%"\httpclient-4.3.4.jar;"%REPO%"\httpcore-4.3.2.jar;"%REPO%"\commons-logging-1.1.3.jar;"%REPO%"\commons-codec-1.6.jar;"%REPO%"\httpmime-4.3.4.jar;"%REPO%"\jopt-simple-3.2.jar;"%REPO%"\ant-1.8.2.jar;"%REPO%"\ant-launcher-1.8.2.jar;"%REPO%"\bcprov-jdk15on-1.47.jar;"%REPO%"\jetty-server-7.3.0.v20110203.jar;"%REPO%"\servlet-api-2.5.jar;"%REPO%"\jetty-continuation-7.3.0.v20110203.jar;"%REPO%"\jetty-http-7.3.0.v20110203.jar;"%REPO%"\jetty-io-7.3.0.v20110203.jar;"%REPO%"\jetty-util-7.3.0.v20110203.jar;"%REPO%"\jetty-servlet-7.3.0.v20110203.jar;"%REPO%"\jetty-security-7.3.0.v20110203.jar;"%REPO%"\guice-3.0.jar;"%REPO%"\javax.inject-1.jar;"%REPO%"\aopalliance-1.0.jar;"%REPO%"\guice-servlet-3.0.jar;"%REPO%"\jcip-annotations-1.0.jar;"%REPO%"\selenium-api-2.43.0.jar;"%REPO%"\json-20080701.jar;"%REPO%"\uadetector-resources-2014.10.jar;"%REPO%"\uadetector-core-0.9.22.jar;"%REPO%"\quality-check-1.3.jar;"%REPO%"\jsr305-2.0.3.jar;"%REPO%"\jsr250-api-1.0.jar;"%REPO%"\arquillian-phantom-driver-1.1.1.Final.jar;"%REPO%"\shrinkwrap-resolver-api-2.0.0.jar;"%REPO%"\shrinkwrap-resolver-spi-2.0.0.jar;"%REPO%"\shrinkwrap-resolver-api-maven-2.0.0.jar;"%REPO%"\shrinkwrap-resolver-spi-maven-2.0.0.jar;"%REPO%"\shrinkwrap-resolver-impl-maven-2.0.0.jar;"%REPO%"\aether-api-1.13.1.jar;"%REPO%"\aether-impl-1.13.1.jar;"%REPO%"\aether-spi-1.13.1.jar;"%REPO%"\aether-util-1.13.1.jar;"%REPO%"\aether-connector-wagon-1.13.1.jar;"%REPO%"\maven-aether-provider-3.0.5.jar;"%REPO%"\maven-model-3.0.5.jar;"%REPO%"\maven-model-builder-3.0.5.jar;"%REPO%"\maven-repository-metadata-3.0.5.jar;"%REPO%"\maven-settings-3.0.5.jar;"%REPO%"\maven-settings-builder-3.0.5.jar;"%REPO%"\plexus-interpolation-1.14.jar;"%REPO%"\plexus-utils-2.0.6.jar;"%REPO%"\plexus-sec-dispatcher-1.4.jar;"%REPO%"\plexus-cipher-1.4.jar;"%REPO%"\wagon-provider-api-2.4.jar;"%REPO%"\wagon-file-2.4.jar;"%REPO%"\wagon-http-lightweight-2.4.jar;"%REPO%"\wagon-http-shared4-2.4.jar;"%REPO%"\shrinkwrap-resolver-impl-maven-archive-2.0.0.jar;"%REPO%"\shrinkwrap-impl-base-1.1.2.jar;"%REPO%"\shrinkwrap-api-1.1.2.jar;"%REPO%"\shrinkwrap-spi-1.1.2.jar;"%REPO%"\shrinkwrap-resolver-api-maven-archive-2.0.0.jar;"%REPO%"\shrinkwrap-resolver-spi-maven-archive-2.0.0.jar;"%REPO%"\plexus-compiler-javac-2.1.jar;"%REPO%"\plexus-compiler-api-2.1.jar;"%REPO%"\plexus-component-api-1.0-alpha-33.jar;"%REPO%"\plexus-classworlds-1.2-alpha-10.jar;"%REPO%"\commons-io-2.4.jar;"%REPO%"\browsermob-proxy-2.0.0.jar
set EXTRA_JVM_ARGUMENTS=
goto endInit

@REM Reaching here means variables are defined and arguments have been captured
:endInit

%JAVACMD% %JAVA_OPTS% %EXTRA_JVM_ARGUMENTS% -classpath %CLASSPATH_PREFIX%;%CLASSPATH% -Dapp.name="browsermob-proxy" -Dapp.repo="%REPO%" -Dbasedir="%BASEDIR%" net.lightbody.bmp.proxy.Main %CMD_LINE_ARGS%
if ERRORLEVEL 1 goto error
goto end

:error
if "%OS%"=="Windows_NT" @endlocal
set ERROR_CODE=1

:end
@REM set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" goto endNT

@REM For old DOS remove the set variables from ENV - we assume they were not set
@REM before we started - at least we don't leave any baggage around
set CMD_LINE_ARGS=
goto postExec

:endNT
@endlocal

:postExec

if "%FORCE_EXIT_ON_ERROR%" == "on" (
  if %ERROR_CODE% NEQ 0 exit %ERROR_CODE%
)

exit /B %ERROR_CODE%
