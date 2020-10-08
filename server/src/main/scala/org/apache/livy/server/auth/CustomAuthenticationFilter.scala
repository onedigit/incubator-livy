package org.apache.livy.server.auth

import javax.servlet.{Filter, FilterChain, FilterConfig, ServletRequest, ServletResponse}
import org.apache.livy.Logging
import org.eclipse.jetty.server.Request
import scala.collection.JavaConverters._

class CustomAuthenticationFilter extends Filter with Logging {

  override def init(filterConfig: FilterConfig): Unit = {
    info("CustomAuthenticationFilter init")
  }

  override def doFilter(request: ServletRequest, response: ServletResponse, chain: FilterChain): Unit = {
    info("CustomAuthenticationFilter doFilter")
    val r = request.asInstanceOf[Request]
    info(s"request headers: ${r.getHeaderNames.asScala.mkString(",")}")
    info(s"Accept-Encoding: ${r.getHeader("Accept-Encoding")}")
  }

  override def destroy(): Unit = {
    info("CustomAuthenticationFilter destroy")
  }
}
